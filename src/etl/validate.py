def validate_walmart_data(df):
    required_columns = [
        "store_id",
        "department_id",
        "date",
        "weekly_sales_amount",
        "sku_id",
        "location_id",
        "demand_units"
    ]

    missing_columns = [col for col in required_columns if col not in df.columns]

    if missing_columns:
        raise ValueError(f"Missing Walmart columns: {missing_columns}")

    if df["date"].isnull().sum() > 0:
        raise ValueError("Walmart date column contains nulls.")

    print("Walmart validation passed.")


def validate_dataco_data(df):
    if "lead_time_days" not in df.columns:
        raise ValueError("lead_time_days column missing in DataCo data.")

    print("DataCo validation passed.")