# -*- coding: utf-8 -*-

"""
Created on Fri Mar  3 14:51:34 2023

@author: Olayinka Abolade
"""

# import modules
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# funtion to read the data set from the csv file
def dataframe():
    gdp_data_frame = pd.read_csv("GDP.csv")
    return gdp_data_frame

# call function to read dataset
gdp_data_frame = dataframe()

# Retrieve list of the first 10 countries in the data frame
country_column = gdp_data_frame["Country "][:10]

country_column_axis = np.arange(len(country_column))

plt.figure(figsize=(16, 13))

plt.bar(country_column_axis - 0.22, gdp_data_frame["2015"][:10], 0.47,  label="2015")
plt.bar(country_column_axis + 0.22, gdp_data_frame["2016"][:10], 0.47, label="2016")

plt.xticks(country_column_axis, country_column, rotation=40)

# Add plot title and labels
plt.title("GDP per capita for 10 countries (2015 & 2016)")

# Labels for the x and y axis
plt.xlabel("Country")
plt.ylabel("GDP per capita in USD")

plt.legend()

# Save plot image
plt.savefig("gdp bar plot.png")

# Display plot
plt.show()
