import pandas as pd
import numpy as np
from pathlib import Path


PROCESSED_PATH = Path("data/processed")


def run_monte_carlo_simulation(n_simulations=1000, random_seed=42):
    np.random.seed(random_seed)

    inventory_policy = pd.read_csv(PROCESSED_PATH / "inventory_policy.csv")

    simulation_results = []

    for _, row in inventory_policy.iterrows():
        sku_id = row["sku_id"]
        avg_demand = row["avg_demand"]
        demand_std = row["demand_std"]
        safety_stock = row["safety_stock"]
        reorder_point = row["reorder_point"]

        stockouts = 0
        total_demand = 0
        fulfilled_demand = 0
        total_cost = 0

        for _ in range(n_simulations):
            simulated_demand = max(
                0,
                np.random.normal(avg_demand, demand_std)
            )

            simulated_lead_time = max(
                0,
                np.random.normal(3.47, 1.67)
            )

            demand_during_lead_time = simulated_demand * simulated_lead_time

            available_inventory = reorder_point + safety_stock

            fulfilled = min(available_inventory, demand_during_lead_time)
            stockout_units = max(0, demand_during_lead_time - available_inventory)

            if stockout_units > 0:
                stockouts += 1

            total_demand += demand_during_lead_time
            fulfilled_demand += fulfilled

            holding_cost = available_inventory * 2
            stockout_cost = stockout_units * 20

            total_cost += holding_cost + stockout_cost

        fill_rate = fulfilled_demand / total_demand if total_demand > 0 else 0
        stockout_probability = stockouts / n_simulations
        avg_cost = total_cost / n_simulations

        simulation_results.append({
            "sku_id": sku_id,
            "abc_class": row["abc_class"],
            "fill_rate": fill_rate,
            "stockout_probability": stockout_probability,
            "avg_simulated_cost": avg_cost
        })

    result_df = pd.DataFrame(simulation_results)

    result_df.to_csv(
        PROCESSED_PATH / "simulation_results.csv",
        index=False
    )

    print("Monte Carlo simulation completed successfully.")
    print(result_df.head())

    return result_df


if __name__ == "__main__":
    run_monte_carlo_simulation()