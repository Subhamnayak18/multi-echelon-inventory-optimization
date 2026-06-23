import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

forecast = pd.read_csv("data/processed/demand_forecast.csv")
inventory = pd.read_csv("data/processed/inventory_policy.csv")
optimized = pd.read_csv("data/processed/optimized_inventory_plan.csv")
simulation = pd.read_csv("data/processed/simulation_results.csv")

st.title("Multi-Echelon Inventory Control Tower")

st.header("Demand Forecast")
st.dataframe(forecast.head())

st.line_chart(forecast[["actual_demand", "forecast_demand"]])

st.header("Inventory Policy")
st.dataframe(inventory.head())

st.header("Optimized Inventory Allocation")
st.dataframe(optimized.head())

echelon_summary = optimized.groupby("echelon")["optimized_inventory_units"].sum()
st.bar_chart(echelon_summary)

st.header("Simulation Performance")
st.dataframe(simulation.head())

st.bar_chart(
    simulation.groupby("abc_class")["stockout_probability"].mean()
)