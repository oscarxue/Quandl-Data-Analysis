#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 12:43:53 2020

@author: oscarxue
"""
import pandas as pd
import quandl

df = quandl.get('FMAC/HPI_NY.1',)   #.1 means first column of the data
print(df)

api_key = 'az9jYTyjE8aUmqX7dAkT'
states = ['CA', 'IL', 'NY','TX']


df = pd.DataFrame

for abbr in states :
    data_label = 'FMAC/HPI_' + abbr +'.1'   #only first column
    print(data_label)
    
    temp_df = quandl.get(data_label, authtoken=api_key)
    
    if df.empty:
        df = temp_df
    else:
        df = pd.concat([df,temp_df], axis = 1 ) # add new columns to df

df.columns= states
print(df)
df.to_excel('FMAC-HPI_CA_IL_NY_TX.xlsx',sheet_name='Sheet1')