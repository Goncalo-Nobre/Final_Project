# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 16:11:20 2020

@author: gonca
"""

# receives a list and stores it in a variable X_new
def run_model(parameter_1, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6):
    import pickle
    import numpy as np
    import pandas as pd
    pkl_filename = "pickle_model.pkl"
    
    
    results = {'Volumes em distribuição':0, 'Envios em distribuição':0, 'Visitas':0,
       'Circuitos':0, 'Dia de Semana':0, 'Dia':0, 'Mes':0, 'Ano':0, 'CMB':0,
       'EVR':0, 'FAO':0, 'GRD':0, 'LIS1':0, 'LIS2':0,
       'LIS3':0, 'LRA':0, 'OPO':0, 'TNV':0, 'VIS':0,
       'VRL':0}

   
    
    Data = parameter_1.split('-')
    
    
    results['Dia'] = int(Data[2])
    
    results['Mes'] = int(Data[1])
    
    results['Ano'] = int(Data[0])
    
    results['Dia de Semana'] = pd.Series(parameter_1).apply(lambda x: pd.to_datetime(x, dayfirst = True).dayofweek).astype(str)
    
    results[parameter_2] = 1
    print(results[parameter_2])
    
    results['Volumes em distribuição'] = parameter_3
    
    results['Envios em distribuição'] = parameter_4
    
    results['Visitas'] = parameter_5
    
    results['Circuitos'] = parameter_6
    
    final_results = np.array(list(results.values()))
    print(final_results)

    
    
    
    # Load from file  -> the trained model
    with open(pkl_filename, 'rb') as file:
        pickle_model = pickle.load(file)
    prediction = pickle_model.predict([final_results])
    
    # makes the prediction based on the trained model, with the new data point
    return prediction

    
    