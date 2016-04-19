from datetime import datetime, time
from pattern.web import * 
from pattern.web import URL, extension, download
import pickle
from selenium import webdriver

#Storing all the days when stock market closes
fin = open('list_of_days.pickle')
complete_list_of_dates = pickle.load(fin)
fin.close()
print datetime.now()


#Changing the directory so that the result files are stored in a convenient place
import os

path = "/home/anne/DataAnalysis/El_Pollo_Loco/2016_Google_Results"

# Check current working directory.
retval = os.getcwd()
print "Current working directory %s" % retval

# Now change the directory
os.chdir( path )

# Check current working directory.
retval = os.getcwd()

print "Directory changed successfully %s" % retval

driver = webdriver.Firefox()

#For loop to iterate through the days:
for date in complete_list_of_dates:
	month = date[0]
	day = date[1]
	year = date[2]

	result = []
	f = open('{}_{}_{}googleresults.pickle'.format(month, day, year), 'w')
	#What to put in the open() URL area for Chipotle: 'https://www.google.com/#q=Chipotle+news&tbs=cdr%3A1%2Ccd_min%3A{}%2F{}%2F{}%2Ccd_max%3A{}%2F{}%2F{}&tbm='.format(month, day-1, year, month, day, year)
	#for El Pollo Loco: https://www.google.com/#q=el+pollo+loco+news&tbs=cdr%3A%2Ccd_min%3A{}%2F{}%2F{}%2Ccd_max%3A{}%2F{}%2F{}&tbm=
	#For Apple: https://www.google.com/#q=apple+news&tbs=cdr%3A1%2Ccd_min%3A{}%2F{}%2F{}%2Ccd_max%3A{}%2F{}%2F{}&tbm=


	driver.get('https://www.google.com/#q=el+pollo+loco+news&tbs=cdr%3A1%2Ccd_min%3A{}%2F{}%2F{}%2Ccd_max%3A{}%2F{}%2F{}&tbm='.format(month, day-1, year, month, day, year))
	time.sleep(2) #note: month, day, year
	driver.find_elements_by_class_name('st')
	for res in driver.find_elements_by_class_name('st'):
		result.append(str(res.text.encode('ascii', 'ignore').decode('ascii')))
	pickle.dump(result, f)
	f.close()

driver.close()
