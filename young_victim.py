import pandas as pd
import matplotlib.pyplot as plt
crime_data=pd.read_csv('https://data.lacity.org/api/views/y8tr-7khq/rows.csv?accessType=DOWNLOAD',header=0)
crime_data.columns =['DR_Number','date_reported','date_occurred','time_occurred','area_ID','area_name','reporting_district','crime_code','crime_code_description','MO_code','victim_age','victim_sex','victim_descent',	'premise_code',	'premise_description','weapon_used_code','weapon_description','status_code','status_description','crime_code1','crime_code2','crime_code3','crime_code4','address','cross_street','location']

young_victim = crime_data[crime_data.victim_age < 18]
young_victim_in2016 = crime_data[(crime_data.victim_age < 18) & (crime_data.date_occurred.str.endswith('16'))]


gender=young_victim_in2016.groupby('victim_sex').time_occurred.sum().plot(kind='bar')
#show different gender victims in 2016#
young_victim_in2016.crime_code.dropna().plot(kind='kde',xlim=(90,600)),plt.show()
#show the kernel density estimate plot for different crime type, here the toppest one is code510#


df=young_victim
df.resample('AS').time_occurred.sum().to_period('A').plot(kind='line')
#young_victim vs year


