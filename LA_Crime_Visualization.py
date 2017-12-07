# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 18:07:26 2017

@author: matth_000
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('https://data.lacity.org/api/views/y8tr-7khq/rows.csv')

df.columns =['DR_Number','date_reported','date_occurred','time_occurred',
             'area_ID','area_name','reporting_district','crime_code',
             'crime_code_description','MO_code','victim_age','victim_sex',
             'victim_descent',	'premise_code',	'premise_description',
             'weapon_used_code','weapon_description','status_code',
             'status_description','crime_code1','crime_code2','crime_code3',
             'crime_code4','address','cross_street','location']

important_crime_types = ['ASSAULT','HOMICIDE','WEAPONS','SEXUAL OFFENSE',
                         'CRIMES AGAINST CHILDREN','THEFT','VEHICLE']

Assault = ['INTIMATE PARTNER - SIMPLE ASSAULT','BATTERY - SIMPLE ASSAULT',
           'ASSAULT WITH DEADLY WEAPON, AGGRAVATED ASSAULT',
           'CHILD ABUSE (PHYSICAL) - SIMPLE ASSAULT', 'OTHER ASSAULT',
           'INTIMATE PARTNER - AGGRAVATED ASSAULT', 
           'CHILD ABUSE (PHYSICAL) - AGGRAVATED ASSAULT',
           'ASSAULT WITH DEADLY WEAPON ON POLICE OFFICER','BATTERY POLICE (SIMPLE)',
           'BATTERY ON A FIREFIGHTER']
Homicide = ['CRIMINAL HOMICIDE','LYNCHING - ATTEMPTED','LYNCHING',
            'MANSLAUGHTER', 'NEGLIGENT']
Weapons = ['BOMB SCARE','SHOTS FIRED AT INHABITED DWELLING',
           'BRANDISH WEAPON','ARSON','DISCHARGE FIREARMS/SHOTS FIRED',
           'WEAPONS POSSESSION/BOMBING',
           'REPLICA FIREARMS(SALE,DISPLAY,MANUFACTURE OR DISTRIBUTE)0132',
           'SHOTS FIRED AT MOVING VEHICLE, TRAIN OR AIRCRAFT',
           'FIREARMS RESTRAINING ORDER (FIREARMS RO)']
Sexual_Offense = ['SODOMY/SEXUAL CONTACT B/W PENIS OF ONE PERS TO ANUS OTH 0007=02',
                  'INDECENT EXPOSURE','RAPE, FORCIBLE',
                  'BATTERY WITH SEXUAL CONTACT',
                  'SEXUAL PENTRATION WITH A FOREIGN OBJECT','LETTERS, LEWD',
                  'RAPE, ATTEMPTED','LEWD CONDUCT','PIMPING','SEX, UNLAWFUL',
                  'ORAL COPULATION','PANDERING',
                  'INCEST (SEXUAL ACTS BETWEEN BLOOD RELATIVES)']
Crimes_against_Children = ['CHILD ABUSE (PHYSICAL) - SIMPLE ASSAULT',
                           'CHILD NEGLECT (SEE 300 W.I.C.)',
                           'CHILD ANNOYING (17YRS & UNDER)',
                           'CRM AGNST CHLD (13 OR UNDER) (14-15 & SUSP 10 YRS OLDER)0060',
                           'CHILD STEALING','CHILD ABUSE (PHYSICAL) - AGGRAVATED ASSAULT',
                           'CHILD ABANDONMENT','DRUGS, TO A MINOR']
Theft = ['THEFT PLAIN - PETTY ($950 & UNDER)',
         'SHOPLIFTING - PETTY THEFT ($950 & UNDER)',
         'EMBEZZLEMENT, PETTY THEFT ($950 & UNDER)',
         'THEFT-GRAND ($950.01 & OVER)EXCPT,GUNS,FOWL,LIVESTK,PROD0036',
         'DEFRAUDING INNKEEPER/THEFT OF SERVICES, $400 & UNDER',
         'SHOPLIFTING-GRAND THEFT ($950.01 & OVER)',
         'THEFT, PERSON','THEFT PLAIN - ATTEMPT',
         'THEFT FROM MOTOR VEHICLE - GRAND ($400 AND OVER)','THEFT OF IDENTITY',
         'BUNCO, GRAND THEFT','BUNCO, PETTY THEFT','THEFT FROM PERSON - ATTEMPT',
         'DISHONEST EMPLOYEE - PETTY THEFT','THEFT FROM MOTOR VEHICLE - ATTEMPT',
         'DISHONEST EMPLOYEE - GRAND THEFT',
         'DEFRAUDING INNKEEPER/THEFT OF SERVICES, OVER $400',
         'GRAND THEFT / INSURANCE FRAUD',
         'THEFT, COIN MACHINE - GRAND ($950.01 & OVER)',
         'GRAND THEFT / AUTO REPAIR','PETTY THEFT - AUTO REPAIR',
         'TILL TAP - GRAND THEFT ($950.01 & OVER)','THEFT, COIN MACHINE - ATTEMPT']
Vehicle = ['VEHICLE - ATTEMPT STOLEN',
           'VEHICLE - STOLEN', 
           'BURGLARY FROM VEHICLE', 
           'THEFT FROM MOTOR VEHICLE - ATTEMPT', 
           'THEFT FROM MOTOR VEHICLE - PETTY ($950 & UNDER)', 
           'THEFT FROM MOTOR VEHICLE - GRAND ($400 AND OVER)', 
           'THROWING OBJECT AT MOVING VEHICLE',
           'BURGLARY FROM VEHICLE, ATTEMPTED']
Other = Assault + Homicide + Crimes_against_Children

df.loc[(df.crime_code_description.isin(Other)),'crime_code_description'] = 'OTHER'
df.loc[(df.crime_code_description.isin(Weapons)),'crime_code_description'] = 'WEAPONS'
df.loc[(df.crime_code_description.isin(Sexual_Offense)),'crime_code_description'] = 'SEXUAL OFFENSE'
df.loc[(df.crime_code_description.isin(Theft)),'crime_code_description'] = 'THEFT'
df.loc[(df.crime_code_description.isin(Vehicle)),'crime_code_description'] = 'VEHICLE'

df = df[df['crime_code_description'].isin(important_crime_types)]

in2014 = df[df.date_occurred.str.endswith('14')]
in2015 = df[df.date_occurred.str.endswith('15')]
in2016 = df[df.date_occurred.str.endswith('16')]
in2017 = df[df.date_occurred.str.endswith('17')]
in16_17 = df[(df.date_occurred.str.endswith('16')) | (df.date_occurred.str.endswith('17'))]
#Pie Chart showing distribution of crimes by type
labels = 'WEAPONS','SEXUAL OFFENSE','THEFT','VEHICLE'
sizes = []
for crime in labels:
    sizes.append(in16_17[in16_17.crime_code_description == crime].count()['crime_code_description'])
sizes = np.array(sizes)
percent_size = 100.*sizes/sizes.sum()
labels = ['{0} - {1:1.2f} %'.format(i,j) for i,j in zip(labels, percent_size)]

fig1,ax1 = plt.subplots()
ax1.pie(sizes, labels = None, autopct = None, shadow = True, labeldistance = 1.2, startangle=90)
ax1.axis('equal')
plt.title('Crime Distribution 2016-2017', weight = 'bold', size = 20)
plt.legend(labels = labels, bbox_to_anchor = (1,0.5), 
           fontsize = 15, bbox_transform = plt.gcf().transFigure, loc = 0)
plt.tight_layout()
plt.show()

