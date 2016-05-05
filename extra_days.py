from datetime import datetime, time
from pattern.web import * 
from pattern.web import URL, extension, download
import pickle
from selenium import webdriver
import os
path = "/home/anne/DataAnalysis/BP/2010_Google_Results"
# Check current working directory.
retval = os.getcwd()
print "Current working directory %s" % retval
# Now change the directory
os.chdir( path )
# Check current working directory.
retval = os.getcwd()
print "Directory changed successfully %s" % retval

#This script is for the days that are blocked due to the captchas in google
#1: Add a few days before the range of missing days, run the code
#2: Once the firefox window opens, enter the 
driver = webdriver.Firefox()
dates = [(7, 21, 2010), (7, 22, 2010), (7, 23, 2010)]
#For loop to iterate through the days:
for date in dates:
	month = date[0]
	day = date[1]
	year = date[2]
	print month, day, year
	result = []
	f = open('{}_{}_{}googleresults.pickle'.format(month, day, year), 'w')
	driver.get('https://www.google.com/#q=BP+British+Petroleum+news&tbs=cdr%3A1%2Ccd_min%3A{}%2F{}%2F{}%2Ccd_max%3A{}%2F{}%2F{}&tbm='.format(month, day-1, year, month, day, year))
	time.sleep(2) #note: month, day, year
	driver.find_elements_by_class_name('st')
	for res in driver.find_elements_by_class_name('st'):
		result.append(str(res.text.encode('ascii', 'ignore').decode('ascii')))
	pickle.dump(result, f)
	f.close()

driver.close()