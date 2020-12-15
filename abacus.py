import csv
import datetime
import collections
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

#GET DATA FROM CSV FILE
#with open('./data/data_short.csv') as data_in:
with open('./data/usage_2020-12-12.csv') as data_in:
	data = list(csv.DictReader(data_in))
'''
#BUILD USAGE DICTIONARY FROM CSV FILE
kwh_str_dict = {} #This will be the dictionary of usage by date,hour

i_date_list = []

for i in data:
	i_space = i['StartDate'].find(' ')
	i_date = i['StartDate'][0:i_space]
	i_month = i['StartDate'][0:(i['StartDate'].find('/'))]
	
	if i_date not in i_date_list:
		i_date_list.append(i_date)
		hour_list = {}
	
		for j in data:
			j_space = j['StartDate'].find(' ')
			j_date = j['StartDate'][0:j_space]
			
			j_colon = j['StartDate'].find(':')
			j_hour = int(j['StartDate'][j_space:j_colon].strip())
			
			try:
				kwh = float(j['Value (kWh)'])
			
			except:
				kwh = float(0)
		
			if j_date == i_date:
				hour_list[j_hour]=(kwh)

		kwh_str_dict[i_date]=hour_list
	kwh = kwh_str_dict
#print(kwh)
'''
def get_datetime(string):
	date = datetime.datetime.strptime(string,'%m/%d/%y %H:%M')
	return(date)

kwh_list = []

for i in data:
	date=i['StartDate']
	datetime_obj = get_datetime(date)
	i.update({'StartDate':datetime_obj})

	try:
		kwh = round(float(i['Value (kWh)']),2)
	except:
		kwh = round(float(0),2)

	kwh_list.append([datetime_obj,kwh])
#print(kwh_list)

years = []
months = []
days = []

for row in kwh_list:
	yr = row[0].year
	mo = row[0].month
	da = row[0].day
	kwh = row[1]

	yr_mo = str(mo)+'/01/'+str(yr)
	yr_mo_da = str(mo)+'/'+str(da)+'/'+str(yr)

	if yr not in years:
		years.append(yr)

	if yr_mo not in months:
		months.append(yr_mo)

	if yr_mo_da not in days:
		days.append(yr_mo_da)

def usage_yearly():
	kwh_years = {}		
	for a in years:
		kwh = 0
		for b in kwh_list:
			b_yr=b[0].year
			if b_yr==a:
				kwh += b[1]
			kwh_years[a]=round(kwh,2)
	return(kwh_years)

def usage_monthly():
	kwh_months = {}		
	for a in months:
		kwh = 0
		for b in kwh_list:
			b_mo=str(b[0].month)+'/01/'+str(b[0].year)
			if b_mo==a:
				kwh += b[1]
			kwh_months[a]=round(kwh,2)
	return(kwh_months)

def usage_daily():
	kwh_days = {}		
	for a in days:
		kwh = 0
		for b in kwh_list:
			b_da=str(b[0].month)+'/'+str(b[0].day)+'/'+str(b[0].year)
			if b_da==a:
				kwh += b[1]
			kwh_days[a]=round(kwh,2)
	return(kwh_days)

#z=usage_daily()
z=usage_monthly()
#z=usage_yearly()
print(z)


date_str = []
x=list(z.keys())
y=list(z.values())

plt.scatter(x,y)
plt.show()

x = np.array(x)
y = np.array(y)


plt.bar(x,y)
plt.xticks(x,x,rotation='vertical',color = 'blue', fontsize ='8')

for i in range(len(z.values())):
    bars = plt.bar(x[i], y[i], .35, align="edge", animated=0.4)
    for rect in bars:
        height = rect.get_height()
        plt.text(rect.get_x(), height, '%d' % int(height), ha='center', va='bottom',fontsize='6')

plt.show()
