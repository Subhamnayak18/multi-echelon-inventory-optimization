from extract import read_walmart_data, read_dataco_data
from transform import clean_walmart_data, clean_dataco_data
from validate import validate_walmart_data, validate_dataco_data
from load import save_staging_data


def main():
    print("Reading raw data...")
    train, features, stores = read_walmart_data()
    dataco = read_dataco_data()

    print("Transforming data...")
    walmart_clean = clean_walmart_data(train, features, stores)
    dataco_clean = clean_dataco_data(dataco)

    print("Validating data...")
    validate_walmart_data(walmart_clean)
    validate_dataco_data(dataco_clean)

    print("Saving staging data...")
    save_staging_data(walmart_clean, dataco_clean)

    print("ETL pipeline completed successfully.")


if __name__ == "__main__":
    main()