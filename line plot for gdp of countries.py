# -*- coding: utf-8 -*-

"""
Created on Fri Mar  3 14:51:34 2023

@author: Olayinka Abolade
"""

# import modules
import pandas as pd
import matplotlib.pyplot as plt

# funtion to read the data set from the csv file
def dataframe():
    gdp_data_frame = pd.read_csv("GDP.csv")
    return gdp_data_frame

# Call function and store data set in a variable called gdp_data_frame
gdp_data_frame = dataframe()

plt.figure(figsize=(12, 9))

# Country list for GDP
countries = ["United States", "United Kingdom", "Australia", "China", "Japan",
            "Nigeria", "Brazil", "South Africa",]

gdp_data = gdp_data_frame[(gdp_data_frame['Country '].isin(countries))]

# Create a list of year from 2007 to 2013
years = [str(year) for year in range(2007, 2014)]

# Retrieve data frame by columns
gdp_data = gdp_data[["Country "] + years]

# Make country index
gdp_data = gdp_data.set_index("Country ").T

# Loop through dataframe and create the plots for the gdp
for country in countries:
    plt.plot(years, gdp_data[country], label=country, marker="o")

# Add plot title and labels
plt.title("GDP per capita of 8 countries (2007 - 2013)")

# Label for the x and y axis
plt.xlabel("Year")
plt.ylabel("GDP per capita in USD")

plt.legend()

# Save plot image
plt.savefig("gdp line plot.jpg")

# Display plot
plt.show()

