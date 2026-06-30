import pandas as pd


def metrics(df):

    print("Rows :", len(df))

    print("Columns :", len(df.columns))

    print("Duplicates :", df.duplicated().sum())

    print("Null Values")

    print(df.isnull().sum())
