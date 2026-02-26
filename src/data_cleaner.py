import pandas as pd

def clean_data():
    df = pd.read_csv("data/raw_data.csv")
    df.dropna(inplace=True)

    df["title_length"] = df["title"].apply(len)

    df.to_csv("data/clean_data.csv", index=False)