#Should return a list with all the days that are viable for 2013, 2014, 2015, 2016
from datetime import datetime, time
import pickle
import os

dates_list = []
days = range(1, 32)
months = range(1, 13)

special_months = [2, 4, 6, 9, 11]

#Storing all the days when stock market closes, applies to 2010 and 2015
fin = open('DaysStockMarketClosed.txt')
closed_days = []
for line in fin:
    old_format = line.strip()
    year = int(old_format[0:4])
    month = int(old_format[5:7])
    day = int(old_format[8:10])
    new_format = (month, day, year) 
    closed_days.append(new_format)
fin.close()

def making_all_the_days(year): #includes the impossible days

	for month in months:
		for day in days:
			dates_list.append((month, day, year))
	return dates_list

def removing_dates(every_single_date_list):
	date_list = []
	for (month, day, year) in every_single_date_list:

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

def filtering_for_weekdays(reasonable_date_list):
	weekdays = []
	for res in reasonable_date_list:
		# print res[2] + res[0] + res[1]
		if datetime(res[2], res[0], res[1]).weekday() in [5, 6]:
			pass
		else:
			weekdays.append((res[0], res[1], res[2]))
	return weekdays

def eliminate_holidays(weekdays):
	DaysStockMarketOpen = []
	for date in weekdays:
		if date in closed_days:
			pass
		else:
			DaysStockMarketOpen.append(date)
	return DaysStockMarketOpen

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

#Generating the list of possible stock-market dates for 2010
year = 2010

inclusive_dates_2010 = making_all_the_days(year)

reasonable_days_2010 = removing_dates(inclusive_dates_2010)

weekdays_2010 = filtering_for_weekdays(reasonable_days_2010)

list_of_days_2010 = eliminate_holidays(weekdays_2010)

final_list_of_dates_2010 = before_today_dates(list_of_days_2010) #the final final list! Whoohoo!
# print final_list_of_dates_2010

#Generating the list of possible stock-market dates for 2010
year = 2011

inclusive_dates_2011 = making_all_the_days(year)

reasonable_days_2011 = removing_dates(inclusive_dates_2011)

weekdays_2011 = filtering_for_weekdays(reasonable_days_2011)

list_of_days_2011 = eliminate_holidays(weekdays_2011)

final_list_of_dates_2011 = before_today_dates(list_of_days_2011) #the final final list! Whoohoo!
# print final_list_of_dates_2011

#Generating the list of possible stock-market dates for 2010
year = 2012

inclusive_dates_2012 = making_all_the_days(year)

reasonable_days_2012 = removing_dates(inclusive_dates_2012)

weekdays_2012 = filtering_for_weekdays(reasonable_days_2012)

list_of_days_2012 = eliminate_holidays(weekdays_2012)

final_list_of_dates_2012 = before_today_dates(list_of_days_2012) #the final final list! Whoohoo!
# print final_list_of_dates_2012

#Generating the list of possible stock-market dates for 2010
year = 2013

inclusive_dates_2013 = making_all_the_days(year)

reasonable_days_2013 = removing_dates(inclusive_dates_2013)

weekdays_2013 = filtering_for_weekdays(reasonable_days_2013)

list_of_days_2013 = eliminate_holidays(weekdays_2013)

final_list_of_dates_2013 = before_today_dates(list_of_days_2013) #the final final list! Whoohoo!
# print final_list_of_dates_2013

#Generating the list of possible stock-market dates for 2010
year = 2014

inclusive_dates_2014 = making_all_the_days(year)

reasonable_days_2014 = removing_dates(inclusive_dates_2014)

weekdays_2014 = filtering_for_weekdays(reasonable_days_2014)

list_of_days_2014 = eliminate_holidays(weekdays_2014)

final_list_of_dates_2014 = before_today_dates(list_of_days_2014) #the final final list! Whoohoo!
# print final_list_of_dates_2014

#Generating the list of possible stock-market dates for 2015
dates_list = [] #resetting the dates list

year = 2015

inclusive_dates_2015 = making_all_the_days(year)

reasonable_days_2015 = removing_dates(inclusive_dates_2015)

weekdays_2015 = filtering_for_weekdays(reasonable_days_2015)

list_of_days_2015 = eliminate_holidays(weekdays_2015)

final_list_of_dates_2015 = before_today_dates(list_of_days_2015) #the final final list! Whoohoo!

#Generating the list of possible stock-market dates for 2015
dates_list = [] #resetting the dates list

year = 2016

inclusive_dates_2016 = making_all_the_days(year)

reasonable_days_2016 = removing_dates(inclusive_dates_2016)

weekdays_2016 = filtering_for_weekdays(reasonable_days_2016)

list_of_days_2016 = eliminate_holidays(weekdays_2016)

final_list_of_dates_2016 = before_today_dates(list_of_days_2016) #the final final list! Whoohoo!

