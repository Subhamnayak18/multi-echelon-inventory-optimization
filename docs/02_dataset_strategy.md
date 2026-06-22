# Dataset Strategy

## Objective

The objective of this phase is to build a realistic data foundation for the Multi-Echelon Inventory Optimization System using a combination of real-world datasets and synthetic enterprise master data.

The project requires:

* Demand data
* Supply chain shipment data
* Warehouse metadata
* Inventory data
* Supplier lead times
* Transportation cost data

The data strategy follows:

Real demand data + Real shipment data + Synthetic enterprise master data

---

## Dataset 1: Walmart Store Sales Forecasting

### Purpose

Used as the primary demand dataset.

This dataset provides historical weekly sales at store and department level.

### Business Usage

Supports:

* Demand forecasting
* Demand variability analysis
* Seasonality detection
* Holiday impact analysis
* Demand aggregation by location

### Files Used

* train.csv
* features.csv
* stores.csv

### Key Fields

* Store
* Dept
* Date
* Weekly_Sales
* Temperature
* Fuel_Price
* CPI
* Unemployment
* IsHoliday

---

## Dataset 2: DataCo Smart Supply Chain

### Purpose

Used as the shipment and logistics dataset.

This dataset provides order fulfillment, delivery performance, and shipment behavior.

### Business Usage

Supports:

* Lead time analysis
* Shipment delay modeling
* Supply chain risk analysis
* Order fulfillment performance
* Delivery SLA analysis

### Files Used

* DataCoSupplyChainDataset.csv

### Key Fields

* Order Date
* Shipping Date
* Delivery Status
* Late Delivery Risk
* Product Price
* Order Region
* Order Country

---

## Synthetic Data Requirements

Public datasets do not provide enterprise inventory planning master tables.

These will be generated synthetically:

* sku_master.csv
* supplier_master.csv
* warehouse_capacity.csv
* lead_time_master.csv
* inventory_snapshot.csv
* transport_cost_matrix.csv
* service_level_policy.csv

---

## Storage Architecture

Raw data:

data/raw/

Staging data:

data/staging/

Processed data:

data/processed/

Synthetic data:

data/synthetic/

---

## Data Integration Strategy

Walmart data will be used as the demand source.

DataCo data will be used as the shipment and lead time source.

Synthetic tables will provide:

* supply chain hierarchy
* warehouse structure
* inventory states
* service-level policies

These will be joined using:

* sku_id
* location_id
* supplier_id
* date

---

## Final Data Model Inputs

The final analytical system will contain:

* historical demand
* shipment lead times
* inventory snapshots
* warehouse capacities
* service-level targets
* transport cost matrix
* supplier constraints
