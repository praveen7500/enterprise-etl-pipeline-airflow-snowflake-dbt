from extract import extract_csv
from validate import validate
from transform import transform
from upload_to_s3 import upload
from load_to_snowflake import load
from logger import logger

FILE = "data/raw/sales.csv"

def run():

    logger.info("Pipeline Started")

    df = extract_csv(FILE)

    validate(df)

    df = transform(df)

    df.to_csv("data/processed/processed_sales.csv", index=False)

    upload("data/processed/processed_sales.csv")

    load()

    logger.info("Pipeline Completed")

if __name__ == "__main__":
    run()
