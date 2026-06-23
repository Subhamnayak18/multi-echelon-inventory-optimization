from fastapi import FastAPI
import pandas as pd

app = FastAPI(title="Inventory Optimization API")


@app.get("/")
def home():
    return {"message": "API is running"}


@app.get("/forecast")
def get_forecast():
    df = pd.read_csv("data/processed/demand_forecast.csv")
    return df.tail(10).to_dict(orient="records")


@app.get("/inventory-policy")
def get_inventory_policy():
    df = pd.read_csv("data/processed/inventory_policy.csv")
    return df.head(20).to_dict(orient="records")


@app.get("/optimization")
def get_optimization():
    df = pd.read_csv("data/processed/optimized_inventory_plan.csv")
    return df.head(20).to_dict(orient="records")


@app.get("/simulation")
def get_simulation():
    df = pd.read_csv("data/processed/simulation_results.csv")
    return df.head(20).to_dict(orient="records")