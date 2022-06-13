"""
PIT-UN Internship
Tidying Data Practice
Week 1
Alyssa Crawford
"""

import pandas as pd, seaborn as sns, os, matplotlib.pyplot as plt


# read all data into dataframes
incarc_data_men = pd.read_excel('data/race_ethnicity_gender_2010.xlsx',
        sheet_name = "Men",
        skiprows = 4)
incarc_data_women = pd.read_excel('data/race_ethnicity_gender_2010.xlsx',
        sheet_name = "Women",
        skiprows = 4)
incarc_data_total = pd.read_excel('data/race_ethnicity_gender_2010.xlsx',
        sheet_name = "Total",
        skiprows = 4)

# isolate only the total values, remove race/ethnicity data
incarc_rates_men = incarc_data_men['Geography', 
        'Total Men : In Correctional Facilities for Adults',
        'Total Population: Male', 
        'Male incarceration rate']
incarc_rates_women = incarc_data_women['Geography', 
        'Total Women : In Correctional Facilities for Adults',
        'Total Population: Female', 
        'Female incarceration rate']
incarc_rates_total = incarc_data_men['Geography', 
        'Total : In Correctional Facilities for Adults',
        'Total Population', 
        'Incarceration rate']

print(incarc_rates_men)