# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 16:53:39 2020

@author: gonca
"""
import pandas as pd
import time

  
data = pd.read_excel('/Users/gonca/OneDrive/Documentos/Final_Project_support/dados_dpd.xlsx')    
#data['Site'].unique()

results = {'Volumes em distribuição':0, 'Envios em distribuição':0, 'Visitas':0,
       'Circuitos':0, 'Dia de Semana':0, 'Dia':0, 'Mes':0, 'Ano':0, 'CMB':0,
       'EVR':0, 'FAO':0, 'GRD':0, 'LIS1':0, 'LIS2':0,
       'LIS3':0, 'LRA':0, 'OPO':0, 'TNV':0, 'VIS':0,
       'VRL':0}


def clean_date(parameter_1):     
    
    Dia, Mes, Ano = parameter_1.split('-')
    
    return int(Dia), int(Mes), int(Ano)
    

Dia, Mes, Ano = clean_date(parameter_1)

results['Dia'] = Dia

results['Mes'] = Mes

results['Ano'] = Ano

results['Dia de Semana'] = time.dayofweek(parameter_1)

results[parameter_2] = 1

results['Volumes em distribuição'] = parameter_3

results['Envios em distribuição'] = parameter_4

results['Visitas'] = parameter_5

results['Circuitos'] = parameter_6

final_results = np.array(results.values())


'''


def dummy_magic(parameter_2):
    dummy_dict = {}  
    locais = list(data['Site'].unique())
    
    for local in locais:
       results[local] = 0
    
    for key in dummy_dict.keys():
      if key == parameter_2:
          dummy_dict[key] += 1
         
    return pd.DataFrame.from_dict(dummy_magic(parameter_2), orient = 'index').T
         



def clean_date(parameter_1):
    
    # Vamos separar a coluna da data por uma com dias, mes e anos
    parameter_1 = pd.to_datetime(parameter_1)
    
    df['Dia'] = parameter_1.dt.day
    df['Mes'] = parameter_1.dt.month
    df['Ano'] = parameter_1.dt.year
    
    # Agora vamos colocar o dia da semana

    df['Dia de Semana'] = df['Data distribuição'].apply(lambda time: time.dayofweek)
    
    # Dropar a data porque ja nao precisamos dela
    df.drop(['Data distribuição'], axis = 1, inplace = True)
    
'''    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    