# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 18:07:26 2017

@author: matth_000
"""

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('https://data.lacity.org/api/views/y8tr-7khq/rows.csv')

df.columns =['DR_Number','date_reported','date_occurred','time_occurred',
             'area_ID','area_name','reporting_district','crime_code',
             'crime_code_description','MO_code','victim_age','victim_sex',
             'victim_descent',	'premise_code',	'premise_description',
             'weapon_used_code','weapon_description','status_code',
             'status_description','crime_code1','crime_code2','crime_code3',
             'crime_code4','address','cross_street','location']

important_crime_types = ['VEHICLE - STOLEN', 'CRIMINAL HOMICIDE', 'ROBBERY', 
                         'WEAPONS POSSESSION/BOMBING', 'RAPE', 'KIDNAPPING',
                         'BATTERY WITH SEXUAL CONTACT', 'PURSE SNATCHING', 'THEFT, PERSON',
                         'THEFT FROM MOTOR VEHICLE']
for i in range(df.crime_code_description.count()):
    if df.crime_code_description.index(i) in ['THEFT FROM MOTOR VEHICLE - GRAND ($400 AND OVER)', 
             'THEFT FROM MOTOR VEHICLE - PETTY ($950 & UNDER)', 
             'THEFT FROM MOTOR VEHICLE - ATTEMPT']:
        i = 'THEFT FROM MOTOR VEHICLE'
    elif df.crime_code_description.index(i) in ['RAPE, FORCIBLE', 'RAPE, ATTEMPTED']:
        i = 'RAPE'
    elif df.crime_code_description.index(i) in ['KIDNAPPING - GRAND ATTEMPT','KIDNAPPING']:
        i = 'KIDNAPPING'
df = df[df['crime_code_description'].isin(important_crime_types)]

in2016 = df[df.date_occurred.str.endswith('16')]

#Pie Chart showing distribution of crimes by type
labels = ('VEHICLE - STOLEN', 'CRIMINAL HOMICIDE', 'ROBBERY', 
'WEAPONS POSSESSION/BOMBING', 'RAPE, FORCIBLE', 'RAPE, ATTEMPTED', 
'KIDNAPPING', 'KIDNAPPING - GRAND ATTEMPT', 'BATTERY WITH SEXUAL CONTACT', 
'PURSE SNATCHING', 'THEFT, PERSON', 'THEFT FROM MOTOR VEHICLE - GRAND ($400 AND OVER)', 
'THEFT FROM MOTOR VEHICLE - PETTY ($950 & UNDER)', 'THEFT FROM MOTOR VEHICLE - ATTEMPT')
sizes
