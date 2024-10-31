import pandas as pd
import matplotlib.pyplot as plt

from lesson1.step_3_aggregate_data.task_solved import aggregate_data

def plot_chart():
    pivot_table = aggregate_data()

    # Use a colormap to assign colors to different genres
    colors = plt.get_cmap('gist_rainbow', len(pivot_table.columns))

    # Create the bar chart
    ax = pivot_table.plot(kind='bar', figsize=(10, 6), color=[colors(i) for i in range(len(pivot_table.columns))])

    # Adding titles and labels
    plt.title('Number of Games by Genre and Platform')
    plt.xlabel('platform')
    plt.ylabel('count')
    plt.xticks(rotation=0)  # Set rotation to 0 for better visibility
    plt.legend(title='Genre', bbox_to_anchor=(1.05, 1), loc='upper left')  # Legend on the right side
    plt.tight_layout()

    # Show the plot
    plt.show()
    print(ax)
    return ax
