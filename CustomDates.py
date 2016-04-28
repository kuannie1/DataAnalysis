#Should return a list with all the days that are viable for 2013, 2014, 2015, 2016
from datetime import datetime, time
import pickle
import os

dates_list = []
days = range(1, 32)
months = range(1, 13)
years = [2010] 

special_months = [2, 4, 6, 9, 11]

def making_all_the_days(): #includes the impossible days
	for year in years:
		for month in months:
			for day in days:
				dates_list.append((month, day, year))
	return dates_list

inclusive_dates = making_all_the_days()


def removing_dates(every_single_date_list):
	date_list = []
	for (month, day, year) in every_single_date_list:
		boolean_leapyear = (month == 2) and (day == 30)
		boolean_nonleapyear = (month == 2) and ((day == 29) or (day == 30))

		if ((year % 4) != 0): #When the year isn't a leap one
			if month == 2 and day == 29:
				pass
			elif month == 2 and day == 30:
				pass
			elif (month in special_months) and (day == 31):
				pass
			else:
				date_list.append((month, day, year))

		else: #When the year is a leap one
			if month == 2 and day == 30:
				pass
			elif (month in special_months) and (day == 31):
				pass
			else:
				date_list.append((month, day, year))
	return date_list 

reasonable_days = removing_dates(inclusive_dates)


def filtering_for_weekdays(reasonable_date_list):
	weekdays = []
	for res in reasonable_date_list:
		# print res[2] + res[0] + res[1]
		if datetime(res[2], res[0], res[1]).weekday() in [5, 6]:
			pass
		else:
			weekdays.append((res[0], res[1], res[2]))
	return weekdays

weekdays = filtering_for_weekdays(reasonable_days)

#Storing all the days when stock market closes
fin = open('DaysStockMarketCosed.txt')
closed_days = []
for line in fin:
    old_format = line.strip()
    year = int(old_format[0:4])
    month = int(old_format[5:7])
    day = int(old_format[8:10])
    new_format = (month, day, year) 
    closed_days.append(new_format)
fin.close()

def eliminate_holidays(weekdays):
	DaysStockMarketOpen = []
	for date in weekdays:
		if date in closed_days:
			pass
		else:
			DaysStockMarketOpen.append(date)
	return DaysStockMarketOpen
list_of_days = eliminate_holidays(weekdays)


def before_today_dates(complete_date_list):
	"""
	Supposed to return the final final list of dates. This list contains every viable stock market date from the begining
	of 2016 to April 11th, 2016. 
	"""
	list_of_dates = []
	for date in complete_date_list:
		year = date[2]
		month = date[0]
		day = date[1]
		if datetime(2016, 4, 11) > datetime(year, month, day):
			list_of_dates.append((month, day, year))
		else:
			break
	return list_of_dates

final_list_of_dates = before_today_dates(list_of_days) #the final final list! Whoohoo!
naming_convention_year = str(years[0])
fin2 = open('list_of_days_{}.pickle'.format(naming_convention_year), 'w')
pickle.dump(final_list_of_dates, fin2)
fin2.close()


path = "/home/anne/DataAnalysis/Sentiment_Dictionaries"
# Check current working directory.
retval = os.getcwd()
print "Current working directory %s" % retval
# Now change the directory
os.chdir( path )
# Check current working directory.
retval = os.getcwd()
print "Directory changed successfully %s" % retval


fin2 = open('list_of_days_{}.pickle'.format(naming_convention_year), 'w')
pickle.dump(final_list_of_dates, fin2)
fin2.close()