import pandas as pd

def filter_data():
    # Load the data
    df = pd.read_csv('dataset.csv')

    #TODO: Count the number of rows before filtering
    original_count = ...

    #TODO: Filter the data to include only PS4, XOne, PC, and WiiU platforms
    filtered_df = ...

    #TODO: Count the number of rows after filtering
    filtered_count = ...

    # Display the counts
    print(f"Number of rows before filtering: {original_count}")
    print(f"Number of rows after filtering: {filtered_count}")

    return filtered_count, filtered_df