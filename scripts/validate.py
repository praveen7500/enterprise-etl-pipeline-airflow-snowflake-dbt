from logger import logger

def validate(df):

    logger.info("Validating dataset")

    if df.empty:
        raise Exception("Dataset is empty")

    if df.isnull().sum().sum() > 0:
        logger.warning("Dataset contains NULL values")

    logger.info("Validation Completed")
