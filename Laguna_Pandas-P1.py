#!/usr/bin/env python
# coding: utf-8

# # PROGRAMMING ASSIGNMENT 3 (PROBLEM 1)
# ## LAGUNA, CARLVINZ E. 
# ### 2ECE-B
# ### SEPTEMBER 10, 2025

# **PROBLEM 1**: Save your file as Surname_Pandas-P1.py
# 
# Using knowledge obtained from the experiment and demonstrations:
# 
# a. Load the corresponding .csv file into a data frame named cars using pandas.
# 
# b. Display the first five and last five rows of the resulting cars.

# In[8]:


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


# In[11]:


#Convert .ipynb file to .py file
get_ipython().system('jupyter nbconvert --to script "Laguna_Pandas-P1.ipynb"')

