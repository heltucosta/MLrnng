# SIMPLE LINEAR REGRESSION 
#Importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split

# Importing the dataset
dataset = pd.read_csv("Salary_Data.csv")
dataset.columns = ['YearsOfExperience', 'Salary']
X = dataset.iloc[:, :-1].values # Matrix of features
y = dataset.iloc[:, 1].values # Dependent variable vector

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/3, random_state = 0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)
