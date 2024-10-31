# Step 1: Load Data with Pandas

## Objective
Learn to read and explore CSV data using Pandas.

## Theory

### Pandas Library
Pandas is a powerful library for data manipulation in Python. One of its main functions, `pandas.read_csv()`, allows us to load data from CSV files into a DataFrame. DataFrames are like tables with rows and columns, making it easy to analyze and manipulate data.

### `read_csv` Function
To load data from a CSV file, use the following code:
```python
import pandas as pd
df = pd.read_csv('data.csv')
```
The path provided in the `pd.read_csv()` function can be either a **relative path** or an **absolute path**:

- **Relative Path**: This is a path that is relative to the current working directory of your script. In the example above, 'data.csv' is a relative path, which means the file data.csv should be located in the same directory as the script that is being executed. If the file is in a subdirectory, you would specify that in the path, like `subfolder/data.csv`.

- **Absolute Path**: This is the full path from the root of the file system to the specific file. For example, an absolute path might look like `C:/Users/Ana/PycharmProjects/Data/data.csv` on Windows or `/home/user/PycharmProjects/Data/data.csv` on Linux. Using an absolute path ensures that the program knows exactly where to find the file, regardless of the current working directory.

Using relative paths is often preferred for portability, especially when sharing your code with others, as it allows for flexibility in file organization.


### Previewing Data with `.head()`
After loading data, you can use .head() to display the first few rows:
```python
print(df.head())
```
This helps verify that the data loaded correctly.

## Task 
- Load the data from `dataset.csv` into a DataFrame.
- Display the first few rows of data.
- Confirm that the columns 'name' and 'platform' are present in the DataFrame.


