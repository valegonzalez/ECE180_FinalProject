import pandas as pd
crime_data=pd.read_csv('https://data.lacity.org/api/views/y8tr-7khq/rows.csv?accessType=DOWNLOAD',header=0)


crime_data.columns =['DR_Number','date_reported','date_occurred','time_occurred','area_ID','area_name','reporting_district','crime_code','crime_code_description','MO_code','victim_age','victim_sex','victim_descent',	'premise_code',	'premise_description','weapon_used_code','weapon_description','status_code','status_description','crime_code1','crime_code2','crime_code3','crime_code4','address','cross_street','location']


young_victim = df[crime_data.victim_age < 18]
female_victim = df[crime_data.victim_sex == 'F']
male_victim = df[crime_data.victim_sex == 'M']
strong_arm = df[crime_data.weapon_description == 'STRONG-ARM (HANDS, FIST, FEET OR BODILY FORCE)']
in2015 = df[crime_data.date_occurred.str.endswith('15')]
young_victim_in2015 = df[(crime_data.victim_age < 18) & (crime_data.date_occurred.str.endswith('15'))]
# categery dataframes are as shown above, I am not sure what data we need, please feel free to change it#

#unique entries for each column#
weapon_types= crime_data.weapon_description.unique()
crime_types=crime_data.crime_code_description.unique()
victim_sex_types=crime_data.victim_sex.unique()
victim_age_types=crime_data.victim_age.unique()
victim_descent_types=crime_data.victim_descent.unique()
