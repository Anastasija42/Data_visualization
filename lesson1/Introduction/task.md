# Lesson Overview

### Goal
In today's digital age, the gaming industry is a colossal force, generating billions in revenue and capturing the attention of millions worldwide. With the constant emergence of new titles and platforms, understanding the landscape of gaming has never been more critical. One of the most effective ways to grasp this dynamic environment is through data visualization.

As gamers, developers, and analysts, we often seek to understand how different genres of games are distributed across various platforms. Platforms like PlayStation 4 (PS4), Xbox One (XOne), PC, and WiiU each offer unique gaming experiences, catering to different audiences and preferences. By visualizing the number of games available on each platform, we can gain valuable insights into trends, preferences, and market opportunities.

In this lesson, we will tackle the challenge of visualizing gaming trends by creating a bar chart that displays the distribution of games by genre across four major gaming platforms.


### Dataset
A CSV file containing information about different games - ``dataset.csv``.
CSV, or Comma-Separated Values, is a widely used file format for storing and exchanging data. It is a simple and effective way to represent tabular data, where each line in the file corresponds to a row in a table, and each value within that line is separated by a comma. CSV files are commonly used for data import/export between different software applications, databases, and data analysis tools.

### Libraries
`matplotlib`and `pandas`

### Target Audience
Beginner to intermediate programmers with basic knowledge of Python.

# Project Setup and Instructions

### Prerequisites
To complete this lesson, you’ll need:
- **Python** (version 3.9 or later recommended)

### Setup

1. **Set Up a Python Environment**
   - It’s always recommended to create a virtual environment to manage dependencies. Run the following commands:
     ```bash
     python3 -m venv env
     env\Scripts\activate  # On Linux, use `source env/bin/activate`
     ```

2. **Install Required Libraries**
   - Install necessary Python packages by running:
     ```bash
     pip install matplotlib pandas
     ```
To perform a quick sanity check to confirm that `matplotlib` and `pandas` are installed, click the check button.
If they are installed, you won’t see any errors; if not, you’ll get an ImportError.
To use the libraries in a script, you have to import them in the following way:
```python
import pandas
import matplotlib
```

### Step-by-Step Guide

#### Step 1: Load Data
   - **Goal**: Load and explore the dataset using Pandas.
   - **File**: `step_1_load_data/`
   - **Instructions**: Learn to read CSV data, understand the structure, and preview the data.
   - **Tests**: Ensure that data loads correctly with the required columns.

#### Step 2: Filter Data by Platform
   - **Goal**: Filter the dataset to include only the selected platforms (PS4, XOne, PC, WiiU).
   - **File**: `step_2_filter_data/`
   - **Instructions**: Filter data using Pandas, keeping only relevant platforms.
   - **Tests**: Verify that only the specified platforms remain.

#### Step 3: Aggregate Data by Genre
   - **Goal**: Aggregate data by counting the number of games per genre for each platform.
   - **File**: `step_3_aggregate_data/`
   - **Instructions**: Use `groupby` and `pivot_table` to structure data for visualization.
   - **Tests**: Confirm the correct data format for plotting.

#### Step 4: Plotting with Matplotlib
   - **Goal**: Create a bar chart showing the number of games by genre and platform.
   - **File**: `step_4_plot_chart/`
   - **Instructions**: Plot a multi-bar chart, with bars representing different platforms.
   - **Tests**: Check that chart elements appear as expected.

#### Step 5: Final Refinements (Optional)
   - **Goal**: Refine and save the chart.
   - **File**: `step_5_refine_chart/`
   - **Instructions**: Add labels, a title, and save the chart as an image file.
   - **Tests**: Validate that the image file is saved with the correct name.

### Running Tests
Each step has a test to verify that your code works as expected.
Just use the check button! :)

I encourage you to attempt each step independently. However, if you encounter any challenges or wish to compare your solution with an example, you can refer to the provided solved tasks.


# Why Visual Insights Matter
- **Market Understanding**: Visual representations help stakeholders comprehend the distribution of games, making it easier to identify popular genres and platforms. This understanding can inform marketing strategies, game development focus, and investment decisions.


- **Consumer Choices**: For gamers, knowing the number of games available across platforms can guide purchasing decisions and enhance their gaming experience. It can also highlight gaps in the market where new games or genres might be well-received.


- **Industry Trends**: Analyzing game distribution over time can reveal trends and shifts in player preferences, helping developers and publishers adapt to changing demands.


- **Strategic Planning**: Game studios can leverage this data to strategize their game releases, ensuring that they align with market demands and maximize their chances of success.

### Let’s get started by clicking the `Next` button!