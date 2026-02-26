import pandas as pd

def generate_report():
    df = pd.read_csv("data/clean_data.csv")

    report = {
        "total_rows": len(df),
        "avg_title_length": df["title_length"].mean()
    }

    print(report)