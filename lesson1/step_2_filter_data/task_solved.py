import pandas as pd

def filter_data():
    # Load the data
    df = pd.read_csv('dataset.csv')

    # Count the number of rows before filtering
    original_count = len(df)

    # Filter the data to include only PS4, XOne, PC, and WiiU platforms
    filtered_df = df[df['platform'].isin(['PS4', 'XOne', 'PC', 'WiiU'])]

    # Count the number of rows after filtering
    filtered_count = len(filtered_df)

    # Display the counts
    print(f"Number of rows before filtering: {original_count}")
    print(f"Number of rows after filtering: {filtered_count}")

    return filtered_count, filtered_df