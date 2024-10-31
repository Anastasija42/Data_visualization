import pandas as pd

def load_data():
    # Load the data
    df = pd.read_csv('dataset.csv')

    # Display the first few rows
    print(df.head())

    # Check for required columns
    required_columns = {'name', 'platform'}
    df_columns = set(df.columns)
    # Show all the columns from the dataset
    print(df_columns)

    # Check if required_columns is a subset of df_columns
    if required_columns <= df_columns:
        print("Dataset has 'name' and 'platform' columns!")
        return 0
    else:
        print("'name' and 'platform' columns are missing!")
        return 1