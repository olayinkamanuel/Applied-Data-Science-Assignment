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

# call function to read dataset
gdp_data_frame = dataframe()

countries = ["United States", "United Kingdom", "Australia", "China", "Japan",
            "Nigeria",]

gdp_data = gdp_data_frame[(gdp_data_frame['Country '].isin(countries))]
    
plt.figure(figsize=(16, 12))

# Plots pie chart
plt.pie(gdp_data["2018"], labels=gdp_data["Country "],autopct='%1.1f%%')

# Title of the plot
plt.title("Pie Chart for GDP/capita of 6 Countries (2018)")

plt.savefig("gdp per capita pie plot.png")

# Display plots
plt.show()


