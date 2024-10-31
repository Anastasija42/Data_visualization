# Step 2: Filter Data by Platform

## Objective
Filter the dataset to only include games for the specified platforms: PS4, XOne, PC, and WiiU.

## Theory

### Filtering in Pandas
Pandas makes it easy to filter data based on specific criteria. We can use the `.isin()` method to filter rows where values in a column match any value in a given list.
### Importance of Filtering
Filtering allows us to narrow down our data to focus on the most relevant parts. In this case, we only want to analyze games available on the PS4, XOne, PC, and WiiU platforms.

It’s generally important to verify the format of the information in the table—ensure that all letters are either in lowercase or uppercase, and check for any missing data. In this dataset, the creators took great care to avoid mistakes, and there are no issues present. However, always remember to perform this check!

Let's consider a simplified dataset of students and their preferred programming languages:

| Name     | Language   |
|----------|------------|
| Alice    | Python     |
| Bob      | Java       |
| Charlie  | JavaScript |
| David    | C++        |
| Eve      | Python     |
| Frank    | Ruby       |

Now, let’s say we want to filter this DataFrame to include only students who prefer the programming languages Python and Java.

```python
# Define the languages of interest
languages_of_interest = ['Python', 'Java']

# Filter the DataFrame
filtered_df = df[df['Language'].isin(languages_of_interest)]
```
This filters the DataFrame to only include rows where the platform column is one of the specified values, so the output would be:

Filtered DataFrame:

| Index | Name   | Language |
|-------|--------|----------|
| 0     | Alice  | Python   |
| 1     | Bob    | Java     |
| 4     | Eve    | Python   |


## Task
- Filter the data to include only rows where the platform column has one of these values: PS4, XOne, PC, WiiU.
- Count the number of rows in the original and filtered dataset.
- Display both counts.

<div class="hint">

Use the ``.isin()`` method on the 'platform' column.

</div>

<div class="hint">

Use the ``len()`` function for counting.

</div>


