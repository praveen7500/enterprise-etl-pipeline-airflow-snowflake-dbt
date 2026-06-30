from scripts.extract import extract_csv

from scripts.transform import transform


def test_transform():

    df = extract_csv("data/raw/sales.csv")

    df = transform(df)

    assert "total_amount" in df.columns
