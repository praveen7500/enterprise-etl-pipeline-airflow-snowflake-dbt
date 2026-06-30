from scripts.extract import extract_csv

from scripts.validate import validate


def test_validation():

    df = extract_csv("data/raw/sales.csv")

    validate(df)
