from scripts.extract import extract_csv


def test_extract():

    df = extract_csv("data/raw/sales.csv")

    assert len(df) > 0
