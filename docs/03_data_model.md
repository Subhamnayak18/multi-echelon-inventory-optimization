# Data Engineering Architecture

## Objective

The objective of this phase is to build a scalable ETL pipeline that transforms raw source data into structured analytical datasets for forecasting, optimization, and simulation.

The pipeline follows a layered architecture:

Raw Layer → Staging Layer → Processed Layer

This architecture ensures data quality, traceability, and reproducibility.

---

## Data Architecture

### Raw Layer

Stores source datasets in original format.

Purpose:

* Preserve source integrity
* Enable reprocessing
* Maintain source lineage

Source files:

### Walmart

* train.csv
* features.csv
* stores.csv

### DataCo

* DataCoSupplyChainDataset.csv

Path:

data/raw/

---

### Staging Layer

Stores cleaned and standardized datasets.

Purpose:

* Standardize column names
* Fix data types
* Handle null values
* Create derived fields
* Remove invalid records

Generated files:

* stg_walmart_demand.csv
* stg_dataco_shipments.csv

Path:

data/staging/

---

### Processed Layer

Stores analytics-ready datasets.

Purpose:

* Aggregated demand tables
* Lead time tables
* Inventory planning tables
* Optimization inputs

Future files:

* fact_demand.csv
* fact_shipments.csv
* dim_store.csv
* dim_sku.csv
* fact_inventory_snapshot.csv

Path:

data/processed/

---

## ETL Pipeline Design

The ETL process is modular.

### Extract Layer

File:

src/etl/extract.py

Responsibilities:

* Read raw CSV files
* Load into memory
* Standardize file access

---

### Transform Layer

File:

src/etl/transform.py

Responsibilities:

* Standardize column names
* Merge Walmart datasets
* Generate SKU IDs
* Generate location IDs
* Calculate demand units
* Calculate shipment lead times

---

### Validation Layer

File:

src/etl/validate.py

Responsibilities:

* Check required columns
* Validate date fields
* Validate lead time calculations
* Validate null handling

---

### Load Layer

File:

src/etl/load.py

Responsibilities:

* Save staging outputs
* Create folder structure if missing
* Preserve intermediate datasets

---

### Pipeline Orchestration

File:

src/etl/run_pipeline.py

Responsibilities:

* Execute full ETL flow
* Ensure sequencing
* Trigger validations
* Save final outputs

---

## Data Quality Rules

The system enforces:

### Walmart Data Rules

* No null dates
* No negative demand
* Valid store IDs
* Valid department IDs

---

### DataCo Rules

* Valid order dates
* Valid shipping dates
* Lead time >= 0
* Valid shipment status

---

## Derived Fields

Generated during ETL:

### Walmart

* sku_id
* location_id
* demand_units

---

### DataCo

* lead_time_days

---

## Business Outputs

The ETL pipeline prepares inputs for:

* Demand forecasting
* Safety stock modeling
* Reorder point calculation
* Inventory optimization
* Simulation modeling
* Dashboarding

---

## Technology Stack

Used in this phase:

* Python
* Pandas
* NumPy
* SQL
* Snowflake (next phase)
