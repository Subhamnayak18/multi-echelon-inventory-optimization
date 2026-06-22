# Exploratory Data Analysis

## Objective

The objective of this phase is to analyze historical demand behavior and supply chain variability to identify patterns required for forecasting and inventory optimization.

The EDA focuses on:

* Demand variability
* Seasonality
* Trend analysis
* SKU contribution
* Lead time behavior
* Delivery delays
* Supply chain risk

---

## Business Questions

This phase answers:

* Which SKUs have the highest demand?
* Which stores contribute the most volume?
* How seasonal is demand?
* How volatile is demand?
* Which shipments are delayed?
* What is the average lead time?
* Which regions have the highest delay risk?

---

## Analytical Areas

### Demand Analysis

Source:

Walmart dataset

Focus:

* Weekly sales trend
* Holiday sales spikes
* Department demand distribution
* Store demand concentration
* Demand volatility

---

### Supply Analysis

Source:

DataCo dataset

Focus:

* Shipment lead time
* Delivery delay frequency
* Region-wise delay risk
* Shipment duration variability

---

## Outputs

This phase will generate:

* Demand trend plots
* Seasonal decomposition
* ABC classification
* Lead time distribution plots
* Delay risk heatmaps
* Forecasting feature insights

---

## Business Impact

EDA identifies demand and supply uncertainty drivers which directly affect:

* Forecast accuracy
* Safety stock
* Reorder point
* Service level
* Inventory optimization

# Forecasting

## Objective

The objective of this phase is to forecast future demand using statistical and machine learning models.

## Models Used

- Moving Average
- ARIMA
- XGBoost

## Evaluation Metrics

- RMSE
- MAPE
- Forecast Bias

## Business Usage

The forecast output will be used for:

- Safety stock calculation
- Reorder point calculation
- Inventory optimization
- Stockout prevention

## Model Selection Logic

The best model is selected based on lowest MAPE and RMSE while monitoring forecast bias.

## Model Performance

| Model | RMSE | MAPE | Bias |
|---|---:|---:|---:|
| XGBoost | 11042 | 1.90% | -4199 |
| Moving Average | 15124 | 2.98% | -2615 |
| ARIMA | 18987 | 3.32% | 10614 |

Selected Model:

XGBoost

Reason:

Lowest MAPE and RMSE.