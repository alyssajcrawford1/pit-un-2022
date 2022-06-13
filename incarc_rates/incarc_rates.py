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

# create ratio column
incarc_rates['Men:Women'] = incarc_rates['Male incarceration rate'] / incarc_rates['Female incarceration rate']

# sort by ratio
incarc_rates.sort_values(by='Men:Women', ascending=False, inplace=True)

plt.figure(figsize=(5,8))
ax = sns.barplot(x="Men:Women", y=incarc_rates.index, data=incarc_rates)
#ax.tick_params(axis='x', rotation=90)
ax.set(xlabel = "Ratio of Male:Female Incarceration Rates", 
        ylabel = "",
        title = "Male:Female Incarceration Rates in US")
sns.set(font_scale = 0.9)
plt.tight_layout()
plt.show()



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