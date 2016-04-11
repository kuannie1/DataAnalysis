import datetime as dt, datetime, time
from pattern.web import * 
from pattern.web import URL, extension, download
import pickle
from selenium import webdriver

#driver = webdriver.PhantomJS(executable_path='/usr/bin/phantomjs')
driver = webdriver.Firefox()
# html_text = download('https://www.google.com/#q=Chipotle+news&tbs=cdr%3A1%2Ccd_min%3A1%2F1%2F2015%2Ccd_max%3A1%2F2%2F2015&tbm=', unicode=False)
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html_text, 'lxml')
# print soup

Jan2_2015 = dt.datetime(2015, 1, 2)
print Jan2_2015
#Mondays:
Jan5_2015 = dt.datetime(2015, 1, 5)
Jan12_2015 = Jan5_2015 + dt.timedelta(days = 7)
Jan19_2015 = Jan5_2015 + dt.timedelta(days = 14)
Jan26_2015 = Jan5_2015 + dt.timedelta(days = 21)

#Tuesdays:
Jan6_2015 = dt.datetime(2015, 1, 6)
Jan13_2015 = Jan6_2015 + dt.timedelta(days = 7)
Jan20_2015 = Jan6_2015 + dt.timedelta(days = 14)
Jan27_2015 = Jan6_2015 + dt.timedelta(days = 21)

#Wednesdays:
Jan7_2015 = dt.datetime(2015, 1, 7)
Jan14_2015 = Jan7_2015 + dt.timedelta(days = 7)
Jan21_2015 = Jan7_2015 + dt.timedelta(days = 14)
Jan28_2015 = Jan7_2015 + dt.timedelta(days = 21)

#Thursdays:
Jan8_2015 = dt.datetime(2015, 1, 8)
Jan15_2015 = Jan8_2015 + dt.timedelta(days = 7)
Jan22_2015 = Jan8_2015 + dt.timedelta(days = 14)
Jan29_2015 = Jan8_2015 + dt.timedelta(days = 21)

#Fridays:
Jan9_2015 = dt.datetime(2015, 1, 9)
Jan16_2015 = Jan9_2015 + dt.timedelta(days = 7)
Jan23_2015 = Jan9_2015 + dt.timedelta(days = 14)
Jan30_2015 = Jan9_2015 + dt.timedelta(days = 21)

#List of days:
Jan_days = [2, 5, 6, 7, 8, 9, 12, 13, 14, 15, 16, 19, 20, 21, 22, 23, 26, 27, 28, 29, 30]

#For loop to iterate through the days:
for day in Jan_days:
	result = []
	f = open('Jan{}_results.pickle'.format(day), 'w')
	driver.get('https://www.google.com/#q=Chipotle+news&tbs=cdr%3A1%2Ccd_min%3A{}%2F{}%2F{}%2Ccd_max%3A{}%2F{}%2F{}&tbm='.format(1, day-1, 2015, 1, day, 2015))
	time.sleep(2)
	driver.find_elements_by_class_name('st')
	for res in driver.find_elements_by_class_name('st'):
		result.append(str(res.text.encode('ascii', 'ignore').decode('ascii')))
	pickle.dump(result, f)
	f.close()

driver.close()

# #not needed?
# class Date():
# 	"""
# 	Represents a date in time

# 	attributes: day, month, year
# 	"""

# 	def __init__(self, string_date): #Takes in the string version of date
# 		self.year = string_date[0:4]
# 		self.month = string_date[5:7]
# 		self.day = string_date[8:10]

# 	def getday(self):
# 		return self.day

# 	def getmonth(self):
# 		return self.month

# 	def getyear(self):
# 		return self.year

# now = Date(str(dt.datetime.now()))
# day = now.getday()
# print day
