from datetime import datetime, time
from pattern.web import * 
from pattern.web import URL, extension, download
import pickle
from selenium import webdriver

driver = webdriver.Firefox()
dates = [(12, 29, 2014), (12, 30, 2014), (12, 31, 2014), (1, 1, 2015), (1, 2, 2015), (1, 3, 2015), (1, 4, 2015), (1, 5, 2015), (1, 6, 2015), (1, 7, 2015), (1, 8, 2015), (1, 9, 2015), (1, 10, 2015)]
#For loop to iterate through the days:
for date in dates:
	month = date[0]
	day = date[1]
	year = date[2]
	print month, day, year
	result = []
	f = open('{}_{}_{}googleresults.pickle'.format(month, day, year), 'w')
	driver.get('https://www.google.com/#q=Chipotle+news&tbs=cdr%3A1%2Ccd_min%3A{}%2F{}%2F{}%2Ccd_max%3A{}%2F{}%2F{}&tbm='.format(month, day-1, year, month, day, year))
	time.sleep(2) #note: month, day, year
	driver.find_elements_by_class_name('st')
	for res in driver.find_elements_by_class_name('st'):
		result.append(str(res.text.encode('ascii', 'ignore').decode('ascii')))
	pickle.dump(result, f)
	f.close()

driver.close()