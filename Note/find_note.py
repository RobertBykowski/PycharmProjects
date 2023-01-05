import pandas as pd
from datetime import datetime

def find_note():
    # Read the CSV file into a DataFrame
    data = pd.read_csv("list_of_note.csv")

    # wyfiltruj kolumny
    df_filtered = data.filter(items=["title", "content"], axis=1)
    print(df_filtered)

find_note()