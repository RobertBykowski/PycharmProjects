import pandas as pd
from datetime import datetime

def find_note():
    # Read the CSV file into a DataFrame
    data = pd.read_csv("list_of_note.csv")

    # Filter the columns
    # df_filtered = data.filter(items=["title", "content"], axis=1)
    # print(df_filtered)

    filtered_df = data.loc[ data[ 'title' ].str.contains("Zakupy") ]

    # Print the resulting DataFrame
    print(filtered_df)

find_note()

