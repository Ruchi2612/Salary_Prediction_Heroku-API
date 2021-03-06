# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# 1. Import Libraries
import numpy as np
import pandas as pd
import pickle

dataset = pd.read_csv('hiring.csv')

# 2. Feature Engineering
dataset['experience'].fillna(0, inplace=True)
dataset['test_score'].fillna(dataset['test_score'].mean(), inplace=True)

X= dataset.iloc[:,:3]

# 3. Converting words to integer values
def convert_to_int(word):
    word_dict = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7,
                 'eight':8, 'nine':9, 'ten':10, 'eleven':11, 'twelve':12, 'zero':0, 0:0}
    return word_dict[word]

X['experience'] = X['experience'].apply(lambda x : convert_to_int(x))

Y = dataset.iloc[:,-1]

# 4. Splitting train-test dataset 
#    (Since we have very small dataet so we will train all available dataset)
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

# 5. Fitting model with training data
regressor.fit(X,Y)

# 6. Saving model to disk
pickle.dump(regressor, open('model.pkl','wb'))

# 7. Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
print(model.predict([[2,9,6]]))