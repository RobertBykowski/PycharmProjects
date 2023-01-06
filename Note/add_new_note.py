import pandas as pd
from datetime import datetime

def add_note():
    # Read the CSV file into a DataFrame
    data = pd.read_csv("list_of_note.csv")

    # Get the last value of the id column and add 1
    last_id = data['id'].iloc[-1] + 1

    # Assign the new id value to the id variable
    id = last_id

    # Get the title and content of the new note from the user
    title = input("Note Title: ")
    content = input("Content: ")

    # Get the current date and time
    current_date = datetime.now()
    custom_format = current_date.strftime("%Y-%m-%d %I:%M %p")

    # Create a new DataFrame with the new note
    df = pd.DataFrame({
        "id": [id],
        "title": [title],
        "content": [content],
        "creat_date": [custom_format],
        "modif_date": [custom_format]
    })

    # Add the new data from the DataFrame to the CSV file
    df.to_csv("list_of_note.csv", mode="a", header=False, index=False, lineterminator="\n")

add_note()