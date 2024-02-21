import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.ensemble import RandomForestClassifier
import joblib

data = pd.read_csv('HR_comma_sep.csv')

missing = data.isnull().sum()

le = preprocessing.LabelEncoder()
data['salary'] = le.fit_transform(data['salary'])
data['Departments '] = le.fit_transform(data['Departments '])

x = data[['satisfaction_level', 'last_evaluation', 'number_project',
       'average_montly_hours', 'time_spend_company', 'Work_accident',
       'promotion_last_5years', 'Departments ', 'salary']]
y = data['left']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=42)

clf = RandomForestClassifier(n_estimators = 100, criterion = 'gini')
clf.fit(x_train,y_train)

joblib.dump(clf, 'model.pkl')
print("Model dumped!")

clf = joblib.load('model.pkl')

# Saving the data columns from training
model_columns = list(x.columns)
joblib.dump(model_columns, 'model_columns.pkl')
print("Models columns dumped!")

