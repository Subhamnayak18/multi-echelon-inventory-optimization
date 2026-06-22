import pandas as pd


def clean_walmart_data(train, features, stores):
    train.columns = train.columns.str.lower()
    features.columns = features.columns.str.lower()
    stores.columns = stores.columns.str.lower()

    train["date"] = pd.to_datetime(train["date"])
    features["date"] = pd.to_datetime(features["date"])

    walmart = train.merge(
        features,
        on=["store", "date", "isholiday"],
        how="left"
    )

    walmart = walmart.merge(
        stores,
        on="store",
        how="left"
    )

    walmart = walmart.rename(columns={
        "store": "store_id",
        "dept": "department_id",
        "weekly_sales": "weekly_sales_amount",
        "type": "store_type",
        "size": "store_size"
    })

    walmart["sku_id"] = (
        "SKU_" +
        walmart["department_id"].astype(str).str.zfill(3)
    )

    walmart["location_id"] = (
        "STORE_" +
        walmart["store_id"].astype(str).str.zfill(3)
    )

    walmart["demand_units"] = (
        walmart["weekly_sales_amount"] / 100
    ).round().astype(int)

    walmart["demand_units"] = walmart["demand_units"].clip(lower=0)

    return walmart


def clean_dataco_data(dataco):
    dataco.columns = (
        dataco.columns
        .str.lower()
        .str.strip()
        .str.replace(" ", "_")
        .str.replace("(", "")
        .str.replace(")", "")
    )

    date_columns = [
        "order_date_dateorders",
        "shipping_date_dateorders"
    ]

    for col in date_columns:
        if col in dataco.columns:
            dataco[col] = pd.to_datetime(dataco[col], errors="coerce")

    if "order_date_dateorders" in dataco.columns and "shipping_date_dateorders" in dataco.columns:
        dataco["lead_time_days"] = (
            dataco["shipping_date_dateorders"] -
            dataco["order_date_dateorders"]
        ).dt.days

    dataco["lead_time_days"] = dataco["lead_time_days"].clip(lower=0)

    return dataco