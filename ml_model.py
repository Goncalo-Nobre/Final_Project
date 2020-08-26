# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 16:11:21 2020

@author: gonca
"""


import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import pickle

dpd_data = pd.read_csv('/Users/gonca/OneDrive/Documentos/Final_Project_support/dpd_data.csv')

dpd_data.drop(['Unnamed: 0'], axis = 1, inplace = True)


X = dpd_data.drop(['CHR18_rounded'], axis= 1)
y = dpd_data['CHR18_rounded']

# define model
forest = RandomForestRegressor(bootstrap = True, criterion = 'mse', max_depth = 10,
                               max_features = 'auto', n_estimators = 200, random_state = 1)

forest.fit(X, y)



#
# Save to file in the current working directory
pkl_filename = "pickle_model.pkl"
with open(pkl_filename, 'wb') as file:
    pickle.dump(forest, file)
    

