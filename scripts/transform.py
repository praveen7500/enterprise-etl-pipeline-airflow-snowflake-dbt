from logger import logger

def transform(df):

    logger.info("Transforming dataset")

    df.columns = [col.lower() for col in df.columns]

    df["total_amount"] = df["quantity"] * df["price"]

    return df
