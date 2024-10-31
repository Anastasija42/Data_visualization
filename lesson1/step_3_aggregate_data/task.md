# Step 3: Aggregate Data by Genre

## Objective
Count the number of games per genre for each platform using a pivot table.

## Theory

### Grouping in Pandas
In Pandas, the `groupby()` method allows us to group data based on one or more columns. It is often used in conjunction with aggregation functions to compute summary statistics.

For example:
```python
grouped_data = df.groupby(['platform', 'genre']).sum()
```
The `groupby()` method is used to split the DataFrame into groups based on the unique values in the specified columns—in this case, platform and genre.
This means that the data will be grouped first by platform (e.g., PS4, XOne) and then by genre (e.g., Action, Adventure), allowing for analysis of counts within each genre on each platform.

We can combine this with the `size()` method which counts the number of occurrences in each group created by `groupby()`.
After grouping, it returns a Series with the count of rows for each combination of platform and genre. For example, if there are 10 Action games on PS4, the count for that group would be 10.

The `reset_index()` method is used to convert the resulting Series back into a DataFrame.
By default, the grouped DataFrame will have a multi-level index based on the grouped columns (platform and genre). The `reset_index()` function transforms this into a flat DataFrame.
The parameter name='count' assigns the name 'count' to the new column created, which holds the number of games for each combination of platform and genre.
The final DataFrame will have three columns: 'platform', 'genre', and 'count'.

<div class="hint">

Combine the three functions to get the final DataFrame.

</div>


### What Are Pivot Tables?
**Pivot tables** are powerful tools used in data analysis to summarize and reorganize data, allowing users to extract meaningful insights from raw information. 

In this context, a pivot table is beneficial because it allows us to effectively summarize and analyze the number of games across different genres for each gaming platform. By organizing the data in this manner, we can quickly see how genres are distributed among platforms, identify trends, and make informed decisions based on the aggregated information.

When creating a pivot table, you'll specify the next parameters:

- **Values**: This parameter will determine what data you want to aggregate.
- **Index**: Here, you will decide which column serves as the row labels in your pivot table.
- **Columns**: This parameter will indicate which data will be represented as column headers.
- **Aggregation Function**: You will select how to summarize the data in the values, such as summing up counts.
- **Fill Value**: This will allow you to define how to handle any missing values in your table.

The function might look something like this:
```python
pivot_table = df.pivot_table(values='column_x', index='column_y', columns='column_z', aggfunc='sum/prod/abs', fill_value=0)
```
You need to decide which parameters are needed in this case.

In this case, using an aggregation function like sum doesn’t change the values in the pivot table since each platform and genre combination is unique. However, aggregation functions are vital in scenarios with multiple entries for the same combination, as they help summarize and condense the data. While it may not apply here, understanding how to use aggregation is crucial for effective data analysis in larger datasets.

There are many different ways to change the structure of the data; I encourage you try also alternative methods to achieve the same results.

### Task
- Create a DataFrame that displays the count of games for each combination of platform and genre.
- Create a pivot table that shows the game counts by genre for each platform, with platforms as columns and genres as rows.
- Display the pivot table.
