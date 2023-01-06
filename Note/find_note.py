import pandas as pd

def find_note():
    # Read the CSV file into a DataFrame
    data = pd.read_csv("list_of_note.csv")

    # Set the display width to 50 characters
    pd.set_option('display.width', 50)

    # Align the text in the "title" and "content" columns to the left
    data["title"] = data["title"].apply(lambda x: x.ljust(10))
    data["content"] = data["content"].apply(lambda x: x.ljust(50))

    # Left-justify the values in the "id" column
    def left_justify_id(value):
        return str(value).ljust(3)

    # Convert the DataFrame to a string and align the columns to the left
    result = data.to_string(index=False, justify='left', formatters={'id': left_justify_id})

    # Print the result
    print(result)

find_note()


