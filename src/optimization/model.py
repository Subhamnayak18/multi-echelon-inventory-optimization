import pandas as pd
from ortools.linear_solver import pywraplp
from pathlib import Path


PROCESSED_PATH = Path("data/processed")


def run_inventory_optimization():
    sku_df = pd.read_csv(PROCESSED_PATH / "optimization_sku_input.csv")

    solver = pywraplp.Solver.CreateSolver("SCIP")

    if solver is None:
        raise RuntimeError("OR-Tools solver not available.")

    factory_inventory = {}
    cw_inventory = {}
    rw_inventory = {}
    store_inventory = {}

    for _, sku in sku_df.iterrows():
        sku_id = sku["sku_id"]

        factory_inventory[sku_id] = solver.NumVar(
            0, solver.infinity(), f"factory_{sku_id}"
        )

        cw_inventory[sku_id] = solver.NumVar(
            0, solver.infinity(), f"cw_{sku_id}"
        )

        rw_inventory[sku_id] = solver.NumVar(
            0, solver.infinity(), f"rw_{sku_id}"
        )

        store_inventory[sku_id] = solver.NumVar(
            0, solver.infinity(), f"store_{sku_id}"
        )

    # Capacity constraints
    solver.Add(
        sum(factory_inventory[sku["sku_id"]] for _, sku in sku_df.iterrows())
        <= 50000
    )

    solver.Add(
        sum(cw_inventory[sku["sku_id"]] for _, sku in sku_df.iterrows())
        <= 40000
    )

    solver.Add(
        sum(rw_inventory[sku["sku_id"]] for _, sku in sku_df.iterrows())
        <= 25000
    )

    solver.Add(
        sum(store_inventory[sku["sku_id"]] for _, sku in sku_df.iterrows())
        <= 10000
    )

    # Multi-echelon flow constraints
    for _, sku in sku_df.iterrows():
        sku_id = sku["sku_id"]

        solver.Add(factory_inventory[sku_id] >= cw_inventory[sku_id])
        solver.Add(cw_inventory[sku_id] >= rw_inventory[sku_id])
        solver.Add(rw_inventory[sku_id] >= store_inventory[sku_id])

    # Service and inventory policy constraints
    for _, sku in sku_df.iterrows():
        sku_id = sku["sku_id"]

        # Store must cover expected demand
        solver.Add(store_inventory[sku_id] >= sku["avg_demand"])

        # Regional warehouse must hold safety buffer
        solver.Add(rw_inventory[sku_id] >= sku["safety_stock"])

        # Total network inventory should meet target inventory
        solver.Add(
            factory_inventory[sku_id]
            + cw_inventory[sku_id]
            + rw_inventory[sku_id]
            + store_inventory[sku_id]
            >= sku["target_inventory"]
        )

    # Objective: minimize holding cost across echelons
    objective = solver.Objective()

    for _, sku in sku_df.iterrows():
        sku_id = sku["sku_id"]

        if sku["abc_class"] == "A":
            priority_factor = 0.95
        elif sku["abc_class"] == "B":
            priority_factor = 1.00
        else:
            priority_factor = 1.10

        objective.SetCoefficient(factory_inventory[sku_id], 1.2 * priority_factor)
        objective.SetCoefficient(cw_inventory[sku_id], 1.8 * priority_factor)
        objective.SetCoefficient(rw_inventory[sku_id], 2.5 * priority_factor)
        objective.SetCoefficient(store_inventory[sku_id], 3.2 * priority_factor)

    objective.SetMinimization()

    status = solver.Solve()

    if status != pywraplp.Solver.OPTIMAL:
        raise RuntimeError("No optimal solution found.")

    results = []

    for _, sku in sku_df.iterrows():
        sku_id = sku["sku_id"]

        results.extend([
            {
                "sku_id": sku_id,
                "abc_class": sku["abc_class"],
                "location_id": "FACTORY_001",
                "echelon": "factory",
                "optimized_inventory_units": round(
                    factory_inventory[sku_id].solution_value(), 2
                ),
                "holding_cost_per_unit": 1.2
            },
            {
                "sku_id": sku_id,
                "abc_class": sku["abc_class"],
                "location_id": "CW_001",
                "echelon": "central_warehouse",
                "optimized_inventory_units": round(
                    cw_inventory[sku_id].solution_value(), 2
                ),
                "holding_cost_per_unit": 1.8
            },
            {
                "sku_id": sku_id,
                "abc_class": sku["abc_class"],
                "location_id": "RW_001",
                "echelon": "regional_warehouse",
                "optimized_inventory_units": round(
                    rw_inventory[sku_id].solution_value(), 2
                ),
                "holding_cost_per_unit": 2.5
            },
            {
                "sku_id": sku_id,
                "abc_class": sku["abc_class"],
                "location_id": "STORE_001",
                "echelon": "store",
                "optimized_inventory_units": round(
                    store_inventory[sku_id].solution_value(), 2
                ),
                "holding_cost_per_unit": 3.2
            }
        ])

    result_df = pd.DataFrame(results)

    result_df = result_df[
        result_df["optimized_inventory_units"] > 0
    ]

    result_df.to_csv(
        PROCESSED_PATH / "optimized_inventory_plan.csv",
        index=False
    )

    print("Optimization completed successfully.")
    print(f"Total optimized cost: {solver.Objective().Value():,.2f}")

    return result_df


if __name__ == "__main__":
    run_inventory_optimization()