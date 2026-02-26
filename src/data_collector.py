import requests
import pandas as pd

def fetch_data():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    data = response.json()
    df = pd.DataFrame(data)

    df.to_csv("data/raw_data.csv", index=False)
    print("Dados coletados")