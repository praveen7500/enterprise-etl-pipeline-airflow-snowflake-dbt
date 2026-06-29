import pandas as pd
from logger import logger

def extract_csv(file_path):
    logger.info(f"Reading file {file_path}")
    df = pd.read_csv(file_path)
    logger.info(f"Rows Loaded : {len(df)}")
    return df
