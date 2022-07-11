import numpy as np
import pandas as pd
import os
from sklearn.ensemble import RandomForestClassifier

# Kaggle Titanic datasets
train_data = pd.read_csv("titanic/data/train.csv")  # contains a "Survived" attribute
test_data = pd.read_csv("titanic/data/test.csv")  # no "Survived" attribute


# RANDOM FOREST
y = train_data["Survived"]

features = ["Pclass", "Sex", "SibSp", "Parch"]
X = pd.get_dummies(train_data[features])

# train using data, build model
model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=1)
model.fit(X, y)

# use model to predict test data survival
X_test = pd.get_dummies(test_data[features])
predictions = model.predict(X_test)



# save model results as csv
output = pd.DataFrame({'PassengerId': test_data.PassengerId, 'Survived': predictions})
output.to_csv('titanic/output/submission1.csv', index=False)