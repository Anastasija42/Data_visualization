# The whole code in one place
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('dataset.csv')
filtered_df = df[df['platform'].isin(['PS4', 'XOne', 'PC', 'WiiU'])]
genre_platform_counts = filtered_df.groupby(['platform', 'genre']).size().reset_index(name='count')
pivot_table = genre_platform_counts.pivot_table(values='count', index='platform', columns='genre', aggfunc='sum',
                                                    fill_value=0)
desired_order = ['PS4', 'XOne', 'PC', 'WiiU']
pivot_table = pivot_table.reindex(desired_order)

colors = plt.get_cmap('gist_rainbow', len(pivot_table.columns))

ax = pivot_table.plot(kind='bar', figsize=(10, 6), color=[colors(i) for i in range(len(pivot_table.columns))])

plt.title('Number of Games by Genre and Platform')
plt.xlabel('platform')
plt.ylabel('count')
plt.xticks(rotation=0)  # Set rotation to 0 for better visibility
plt.legend(title='Genre', bbox_to_anchor=(1.05, 1), loc='upper left')  # Legend on the right side
plt.tight_layout()

plt.savefig('games_chart.png')
plt.show()