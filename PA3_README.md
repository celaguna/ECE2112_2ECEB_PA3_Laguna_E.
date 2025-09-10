# Programming Assignment 3

**Student Name:** Laguna, Carlvinz E.  
**Section:** 2ECE-B  
**Course Code:** ECE2112  

---

## Intended Learning Outcomes
1. To identify the codes and functions incorporated in the Pandas library.
2. To be able to apply and use the different codes and functions in creating a Python program using a
Pandas library.

---

## What to Expect
This README documents two Python programs:
1. Problem 1 (loading a CSV file into a pandas DataFrame and displaying rows)
2. Problem 2 (extracting specific information from the DataFrame using subsetting, slicing, and indexing)

Each section includes the actual code with line-by-line explanations inside the code comments, describing the process and why each function or operation is used.

---

## Table of Contents
1. [Intended Learning Outcomes](#intended-learning-outcomes)  
2. [What to Expect](#what-to-expect)  
3. [Problem 1](#problem-1)  
4. [Problem 2](#problem-2)  
5. [Conclusion](#-conclusion)
6. [Programming Assignment 3 (Problem 1) .py file](Laguna_Pandas-P1.py)
7. [Programming Assignment 3 (Problem 2) .py file](Laguna_Pandas-P2.py)

---

## Problem 1
### Problem Description
The goal of this problem is to load a .csv file into a pandas DataFrame and explore its contents. Specifically, the task is to create a DataFrame named cars and display its first five and last five rows. This introduces the concept of data loading and basic inspection in pandas, giving practice with the read_csv() function and DataFrame display methods.

### Code

```python
# Import the pandas library and give it the alias 'pd'
import pandas as pd

# a. Load the corresponding .csv file into a data frame named cars using pandas.
# Load the CSV file named "cars.csv" into a DataFrame called 'cars'
cars = pd.read_csv("cars.csv")

# b. Display the first five and last five rows of the resulting cars.
# Concatenate the first five and last five rows into one DataFrame
cars = pd.concat([cars.head(), cars.tail()])

# Display the resulting DataFrame
cars
```

**Step 1: Import the pandas library**
- We import the pandas library and assign it the alias pd.
- This makes pandas available throughout the script, allowing us to work with CSV files and DataFrames.

```python
import pandas as pd
```
**Step 2: Load the CSV file into a DataFrame**
- pd.read_csv("cars.csv") reads the file named cars.csv and stores it in a DataFrame called cars.
- This creates the main dataset we will manipulate to extract the first and last five rows.

```python
cars = pd.read_csv("cars.csv")
```
**Step 3: Concatenate the first and last five rows**
- pd.concat([cars.head(), cars.tail()]) combines the first five rows (head()) and last five rows (tail()) into a single DataFrame.
- This gives us one clean table with only the first and last portions of the dataset, as required.

```python
cars = pd.concat([cars.head(), cars.tail()])
```
**Step 4: Display the resulting DataFrame**
- Writing cars as the last line of the script tells pandas to render the DataFrame as a formatted table.
- This displays the extracted rows in a neat tabular format without needing print().

```python
cars
```
**Step 5: Convert .ipnyb to .py**

```python
!jupyter nbconvert --to script "PA3.1.ipynb"
```

## Takeaways
1. import pandas as pd allows us to use pandas for data analysis with an easy alias.
2. pd.read_csv() is used to load CSV files directly into a DataFrame for easy manipulation.
3. .head() extracts the first five rows of a DataFrame, useful for quickly inspecting data.
4. .tail() extracts the last five rows of a DataFrame, often used to check dataset endings.
5. pd.concat() can combine multiple DataFrames (e.g., head and tail) into one table.
6. Displaying the DataFrame variable (e.g., cars) directly outputs a neat, tabular view without using print().

---

## Problem 2
### Problem Description
The goal of this problem is to extract specific information from the cars DataFrame using subsetting, slicing, and indexing operations. The tasks include displaying rows with odd-numbered columns, finding the row that contains the model ‘Mazda RX4’, checking the number of cylinders in the model ‘Camaro Z28’, and determining both the number of cylinders and gear types for the models ‘Mazda RX4 Wag’, ‘Ford Pantera L’, and ‘Honda Civic’. This introduces the concept of data selection and filtering in pandas, demonstrating how to navigate, subset, and analyze tabular data effectively.

### Code

```python
# Import the pandas library and assigns it the alias 'pd'
import pandas as pd

# Load the CSV file into a DataFrame called 'cars'
cars = pd.read_csv("cars.csv")

# a. First five rows with odd-numbered columns (1, 3, 5, 7…)
# Select the first 5 rows and only the odd-numbered columns (1, 3, 5…)
odd_columns = cars.iloc[:5, ::2]

# Display the resulting DataFrame 'odd_columns'
odd_columns

# b. Row containing 'Mazda RX4'
# Filter the DataFrame to only include rows where the 'Model' is 'Mazda RX4'
mazda_rx4 = cars[cars['Model'] == 'Mazda RX4']

# Display the row containing the 'Mazda RX4'
mazda_rx4

# c. Cylinders of 'Camaro Z28'
# Select the 'Model' and 'cyl' columns where the 'Model' is 'Camaro Z28'
camaro_cyl = cars.loc[cars['Model'] == 'Camaro Z28', ['Model', 'cyl']]

# Display the DataFrame with 'Camaro Z28' and its cylinder value
camaro_cyl

# d. Cylinders and gear type of selected models
# Create a list of the three specific car models we want to check
selected_models = ['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']

# Filter rows to only include the selected models, showing 'Model', 'cyl', and 'gear'
cyl_gear_info = cars.loc[cars['Model'].isin(selected_models), ['Model', 'cyl', 'gear']]

# Display the DataFrame with cylinders and gear type for the selected models
cyl_gear_info
```

**Step 1: Import the pandas library**
- We import the pandas library and give it the alias pd.
- This makes all pandas DataFrame functions available for the rest of the code.

```python
import pandas as pd
```
**Step 2: Load the CSV file into a DataFrame**
- pd.read_csv("cars.csv") reads the dataset into a DataFrame called cars.
- This serves as the main dataset for all subsetting, slicing, and indexing tasks.

```python
cars = pd.read_csv("cars.csv")
```
**Step 3: Extract first five rows with odd-numbered columns**
- cars.iloc[:5, ::2] selects the first 5 rows and every other column starting from index 0 (1st, 3rd, 5th…).
- This produces the required subset for part (a).

```python
odd_columns = cars.iloc[:5, ::2]
```
**Step 4: Display the odd-numbered column subset**
- Writing odd_columns outputs the resulting DataFrame.
- This displays the answer to part (a) in a neat table.

```python
odd_columns
```
**Step 5: Filter for Mazda RX4 row**
- cars[cars['Model'] == 'Mazda RX4'] selects rows where the Model column matches 'Mazda RX4'.
- This extracts the required row for part (b).

```python
mazda_rx4 = cars[cars['Model'] == 'Mazda RX4']
```
**Step 6: Display the Mazda RX4 row**
- Writing mazda_rx4 shows the filtered row as a table.
- This is the complete answer for part (b).

```python
mazda_rx4
```
**Step 7: Find Camaro Z28 cylinders**
- cars.loc[cars['Model'] == 'Camaro Z28', ['Model', 'cyl']] filters rows where the model is 'Camaro Z28' and only returns the Model and cyl columns.
- This gives the cylinder count for Camaro Z28, solving part (c).

```python
camaro_cyl = cars.loc[cars['Model'] == 'Camaro Z28', ['Model', 'cyl']]
```
**Step 8: Display Camaro Z28 cylinders**
- Writing camaro_cyl outputs the DataFrame with Camaro Z28 and its cylinder count.
- This answers part (c).

```python
camaro_cyl
```
**Step 9: Create a list of selected models**
- We define a list of models: 'Mazda RX4 Wag', 'Ford Pantera L', and 'Honda Civic'.
- This list will be used to filter the DataFrame for part (d).

```python
selected_models = ['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']
```
**Step 10: Filter DataFrame for selected models**
- cars.loc[cars['Model'].isin(selected_models), ['Model', 'cyl', 'gear']] filters rows where the Model matches any in selected_models.
- It only selects the Model, cyl, and gear columns to give the required info.

```python
cyl_gear_info = cars.loc[cars['Model'].isin(selected_models), ['Model', 'cyl', 'gear']]
```
**Step 11: Display cylinders and gear type for selected models**
- Writing cyl_gear_info shows the result in table format.
- This completes part (d).

```python
cyl_gear_info
```
**Step 5: Convert .ipnyb to .py**

```python
!jupyter nbconvert --to script "PA3.1.ipynb"
```

## Takeaways
1. iloc is used for slicing rows and columns by position, making it useful for selecting specific patterns like odd-numbered columns.
2. Boolean indexing (cars['Model'] == 'Mazda RX4') allows filtering rows based on conditions.
3. .loc is used to filter rows by labels and to choose specific columns at the same time.
4. .isin() is helpful for filtering multiple values in one column at once.
5. Assigning subsets (like odd_columns, mazda_rx4, etc.) keeps the code clean and makes outputs reusable.
6. Displaying DataFrame variables directly provides neat tabular output without using print().

---

# 📌 Conclusion

In this assignment, I implemented and explained two Python problems in detail:

1. **Problem 1 – Data Loading and Inspection** → Demonstrated how to use pandas’ read_csv() function to load a dataset into a DataFrame and explore its contents. The task focused on extracting and displaying the first five and last five rows, introducing basic inspection tools such as .head() and .tail().
2. **Problem 2 – Subsetting, Slicing, and Indexing** → Showed how to apply pandas operations like iloc, boolean indexing, .loc, and .isin() to extract specific rows, columns, and values from the dataset. This problem highlighted how to filter by conditions, retrieve single values, and select multiple items at once.

Across both problems, several important data analysis concepts were reinforced:
- DataFrames are the core pandas structure for handling tabular data.
- Indexing and slicing allow precise control over row and column selection.
- Boolean filtering and .isin() provide flexible ways to extract rows that meet specific conditions.
- Concatenation with pd.concat() can be used to combine multiple subsets into a single table.
- Displaying DataFrames directly (without print()) results in a cleaner, more professional tabular format.

Overall, these exercises taught me how to load, inspect, and manipulate real datasets using pandas. They also reinforced the importance of documenting code step by step, making solutions easier to understand, reusable, and ready for future data analysis tasks.

---
