import numpy as np
import pandas as pd
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm

# Kaggle Titanic datasets
train_data = pd.read_csv("titanic/data/train.csv")  # contains a "Survived" attribute
test_data = pd.read_csv("titanic/data/test.csv")  # no "Survived" attribute

# Create a sex column encoded numerically
train_data['Sex2'] = train_data.Sex.apply(lambda x: 0 if x == 'male' else 1)
test_data['Sex2'] = test_data.Sex.apply(lambda x: 0 if x == 'male' else 1)

# Fill age N/As
train_data['Age'] = train_data['Age'].fillna(train_data['Age'].mean())
test_data['Age'] = test_data['Age'].fillna(train_data['Age'].mean())


# Grab features to use in models
y = train_data["Survived"]
features = ["Pclass", "SibSp", "Parch", "Sex2", "Age"] # , "Fare"]




# RANDOM FOREST
# train using data, build model
X = pd.get_dummies(train_data[features])
model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=1)
model.fit(X, y)

# use model to predict test data survival
X_test = pd.get_dummies(test_data[features])
predictions = model.predict(X_test)

# save model results as csv
output = pd.DataFrame({'PassengerId': test_data.PassengerId, 'Survived': predictions})
output.to_csv('titanic/output/submission1.csv', index=False)



# SUPPORT VECTOR MACHINES
# train model using data
clf = svm.SVC()
clf.fit(X, y)

# use model to predict test data survival
predictions2 = clf.predict(X_test)

# save model results as csv
output2 = pd.DataFrame({'PassengerId': test_data.PassengerId, 'Survived': predictions2})
output2.to_csv('titanic/output/submission2.csv', index=False)