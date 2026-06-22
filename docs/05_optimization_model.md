# Inventory Policy Logic

This phase calculates inventory policy parameters for each SKU.

Includes:

- Safety stock
- Reorder point
- Target inventory

Logic uses:

- Demand variability
- Lead time variability
- ABC service level targets

These outputs become constraints for the optimization engine.