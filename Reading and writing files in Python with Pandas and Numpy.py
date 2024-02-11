# -*- coding: utf-8 -*-
"""
Reading and writing files in Python with Pandas and Numpy
Spyder version 5.3.3
"""

# We will use pandas for this video, see Absolute Programming Basics if you need a refresh on some concepts

import pandas as pd
import numpy as np

# Start by importing the dataset

pd.read_csv("C:\Videos\Data\Messy Office Data.csv")

# Notice how the output is shown in the console, but we cannot interact with it
# pd.read_csv allows us to read the csv from a file
# However, if we want to use it later, we need to store it into a variable

messy_data = pd.read_csv("C:\Videos\Data\Messy Office Data.csv")

# Now, a pandas dataframe has been created to store the data
# Why importing data into Python? It allows us to use all Python tools plus a lot of automation
# Imagine that this is a file that needs to be corrected every single time
# We can apply the corrections running the script instead
# Take a second to look at the dataset and notice some corrections that need to be made
# Let's start with the last record, Detroit should be capitalized

messy_data["Office"] = messy_data["Office"].str.title()

# Print the dataset to ensure that itwent through
print(messy_data)

# What about Dustin? Let's assume that this was a typo on a survey, and we meant Austin
# We can change Dustin to Austin using loc
messy_data.loc[messy_data["Office"] == "Dustin", "Office"] = "Austin"

# Assume we know we want to keep the original rating, but add the number of employees
# There are multiple ways of doing this, but in this scenario, we will take the minimum rating and add employees with groupby

clean_data = messy_data.groupby("Office", as_index = False).agg(Rating = ("Rating", np.min),
                                              Employees = ("Employees", np.sum))

# We can see how the data is now more consistent, what about the data types?
clean_data.dtypes

# We may want Office to be a string instead of an object
clean_data["Office"] = clean_data["Office"].astype('str')

# Let's check the data types again
clean_data.dtypes

# We have ensured that the data is a string, even though dtypes will still show it as an object
# Finally, ratings can have decimals, so we may want to relax the integer constrain
clean_data["Rating"] = clean_data["Rating"].astype("float")

# Now, we have done all the transformations that we needed, we can go ahead and write the new file
clean_data.to_excel('C:\Videos\Data\Clean Office Data.xlsx')

# Print a confirmmation text at the end of the script
print("Script executed successfuly")