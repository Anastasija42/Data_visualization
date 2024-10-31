import pandas as pd
from lesson1.step_2_filter_data.task_solved import filter_data

def aggregate_data():
    # Load the filtered data
    _, filtered_df = filter_data()

    #TODO: Group by platform and genre, then count the number of games
    genre_platform_counts = ...

    # Display the results
    print(genre_platform_counts)

    #TODO: Change the structure so the count is shown by genre and platform
    pivot_table = genre_platform_counts.pivot_table(values='...', index='...', columns='...', aggfunc='sum',
                                                    fill_value=0)
    # Sort the pivot table in the desired order
    desired_order = ['PS4', 'XOne', 'PC', 'WiiU']
    pivot_table = pivot_table.reindex(desired_order)

    # Check the pivot table
    print(pivot_table)

    return pivot_table