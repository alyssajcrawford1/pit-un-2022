import numpy as np
import pandas as pd
import os

# Kaggle Titanic datasets
train_data = pd.read_csv("titanic/data/train.csv")  # contains a "Survived" attribute
test_data = pd.read_csv("titanic/data/test.csv")  # no "Survived" attribute



# TEST THEORY: Women survive and men die
women = train_data.loc[train_data.Sex == 'female']["Survived"]
rate_women = sum(women)/len(women)
print("% of women who survived:", rate_women)

men = train_data.loc[train_data.Sex == 'male']["Survived"]
rate_men = sum(men)/len(men)
print("% of men who survived:", rate_men)



