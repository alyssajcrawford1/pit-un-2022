'''
PIT-UN Internship
Tidying Data Practice
Week 1
Alyssa Crawford
'''

import pandas as pd, seaborn as sns, os, matplotlib.pyplot as plt


# read all data into dataframes
incarc_data_men = pd.read_excel('data/race_ethnicity_gender_2010.xlsx',
        sheet_name = 'Men',
        skiprows = 4,
        skipfooter = 1)
incarc_data_women = pd.read_excel('data/race_ethnicity_gender_2010.xlsx',
        sheet_name = 'Women',
        skiprows = 4,
        skipfooter = 1)

# isolate only the total rate values, remove race/ethnicity data
incarc_rates_men = incarc_data_men[['Geography', 'Male incarceration rate']].set_index('Geography')
incarc_rates_women = incarc_data_women[['Geography', 'Female incarceration rate']].set_index('Geography')

# join the two dataframes on geography column
incarc_rates = incarc_rates_men.copy()
incarc_rates = incarc_rates.join(incarc_rates_women)

print(incarc_rates)



'''
Would have worked if data permitted a non-binary interpretation of gender.
Unfortunately, although the incarcerated population data did not add up to the
sum of incarcerated men + women, the given total population of US residents was
equal to the sum of US men + women.

incarc_data_total = pd.read_excel('data/race_ethnicity_gender_2010.xlsx',
        sheet_name = 'Total',
        skiprows = 4,
        skipfooter = 1)

incarc_pop_other = (incarc_data_total['Total : In Correctional Facilities for Adults']
        - incarc_data_men['Total Men : In Correctional Facilities for Adults']
        - incarc_data_women['Total Women : In Correctional Facilities for Adults'])
total_pop_other = (incarc_data_total['Total Population']
        - incarc_data_men['Total Population: Male']
        - incarc_data_women['Total Population: Female'])
incarc_rates_other = incarc_pop_other / total_pop_other * 100000

print(incarc_pop_other)
print(total_pop_other)
'''