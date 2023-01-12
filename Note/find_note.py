import pandas as pd



def display_note():
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

# def find_note(title, content):
#
#     # Read the CSV file into a DataFrame
#     data = pd.read_csv("list_of_note.csv")
#     show_line = data.loc[ data[title] == content ]
#     print(show_line)
def find_note(name_row, content):
    # Read the CSV file into a DataFrame
    data = pd.read_csv("list_of_note.csv")
    pd.set_option('display.width', 50)
    # Use the 'str.contains()' function to search for the specified content in the 'content' column
    show_line = data[data[name_row].str.contains(content, case=False)]
    print(show_line)

# display_note()
element_1 = input("Podaj element, po którym chcesz szukać| id,title,content|: ")
element_2 = input("Podaj tresć: ")
find_note(element_1, element_2)


