from pathlib import Path


STAGING_PATH = Path("data/staging")


def save_staging_data(walmart, dataco):
    STAGING_PATH.mkdir(parents=True, exist_ok=True)

    walmart.to_csv(STAGING_PATH / "stg_walmart_demand.csv", index=False)
    dataco.to_csv(STAGING_PATH / "stg_dataco_shipments.csv", index=False)

    print("Staging files created successfully.")