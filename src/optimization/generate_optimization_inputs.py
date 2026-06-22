import pandas as pd
import numpy as np
from pathlib import Path

PROCESSED_PATH = Path("data/processed")
PROCESSED_PATH.mkdir(parents=True, exist_ok=True)

inventory_policy = pd.read_csv(PROCESSED_PATH / "inventory_policy.csv")

locations = pd.DataFrame({
    "location_id": ["FACTORY_001", "CW_001", "RW_NORTH", "RW_SOUTH", "STORE_001"],
    "echelon": ["factory", "central_warehouse", "regional_warehouse", "regional_warehouse", "store"],
    "capacity_units": [50000, 40000, 25000, 25000, 10000],
    "holding_cost_per_unit": [1.2, 1.8, 2.5, 2.5, 3.2]
})

routes = pd.DataFrame({
    "from_location": ["FACTORY_001", "CW_001", "CW_001", "RW_NORTH", "RW_SOUTH"],
    "to_location": ["CW_001", "RW_NORTH", "RW_SOUTH", "STORE_001", "STORE_001"],
    "transfer_cost_per_unit": [0.8, 1.2, 1.3, 1.6, 1.7]
})

sku_subset = inventory_policy.head(20).copy()

sku_subset["moq"] = 100
sku_subset["stockout_cost_per_unit"] = np.where(
    sku_subset["abc_class"] == "A", 25,
    np.where(sku_subset["abc_class"] == "B", 15, 8)
)

sku_subset.to_csv(PROCESSED_PATH / "optimization_sku_input.csv", index=False)
locations.to_csv(PROCESSED_PATH / "location_master.csv", index=False)
routes.to_csv(PROCESSED_PATH / "route_master.csv", index=False)

print("Optimization input files created.")