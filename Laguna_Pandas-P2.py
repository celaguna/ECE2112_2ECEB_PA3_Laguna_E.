#!/usr/bin/env python
# coding: utf-8

# # PROGRAMMING ASSIGNMENT 3 (PROBLEM 2)
# ## LAGUNA, CARLVINZ E. 
# ### 2ECE-B
# ### SEPTEMBER 10, 2025

# **PROBLEM 2**: Save your file as Surname_Pandas-P2.py
# 
# Using the dataframe cars in problem 1, extract the following information using subsetting, slicing and
# indexing operations.
#     
# a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7…) of cars.
# 
# b. Display the row that contains the ‘Model’ of ‘Mazda RX4’.
#     
# c. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?
# 
# d. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4
# Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have

# In[4]:


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

