from datetime import datetime, time
from pattern.web import * 
from pattern.web import URL, extension, download
import pickle
from selenium import webdriver

driver = webdriver.Firefox()


fin = open('list_of_days_2010.pickle')
complete_list_of_dates_2010 = pickle.load(fin)
fin.close()

fin2 = open('list_of_days_2015.pickle')
complete_list_of_dates_2015 = pickle.load(fin2)
fin2.close()



#Changing the directory so that the headline files are stored in a convenient place
import os

path = "/home/anne/DataAnalysis/El_Pollo_Loco/2015_headlines"

# Check current working directory.
retval = os.getcwd()
print "Current working directory %s" % retval

# Now change the directory
os.chdir( path )

# Check current working directory.
retval = os.getcwd()

print "Directory changed successfully %s" % retval

company = 'El_Pollo_Loco'


#For loop to iterate through the days:
for date in complete_list_of_dates_2015:
	month = date[0]
	day = date[1]
	year = date[2]

	result = []
	f = open('{}_{}_{}_{}_headlines.pickle'.format(company, month, day, year), 'w')
	#What to put in the open() URL area for Chipotle: 'https://www.google.com/#q=Chipotle+news&tbs=cdr%3A1%2Ccd_min%3A{}%2F{}%2F{}%2Ccd_max%3A{}%2F{}%2F{}&tbm='.format(month, day-1, year, month, day, year)
	#for El Pollo Loco: https://www.google.com/#q=el+pollo+loco+news&tbs=cdr%3A%2Ccd_min%3A{}%2F{}%2F{}%2Ccd_max%3A{}%2F{}%2F{}&tbm=
	#For Apple: https://www.google.com/#q=apple+news&tbs=cdr%3A1%2Ccd_min%3A{}%2F{}%2F{}%2Ccd_max%3A{}%2F{}%2F{}&tbm=

	driver.get('https://www.google.com/#q=el+pollo+loco+news&tbs=cdr%3A1%2Ccd_min%3A{}%2F{}%2F{}%2Ccd_max%3A{}%2F{}%2F{}&tbm='.format(month, day-1, year, month, day, year))
	time.sleep(2) #note: month, day, year
	driver.find_elements_by_class_name("r")
	for res in driver.find_elements_by_class_name('r'):
		result.append(str(res.text.encode('ascii', 'ignore').decode('ascii')))
	pickle.dump(result, f)
	f.close()




#Changing the directory so that the URL sponsor(?) files are stored in a convenient place
path = "/home/anne/DataAnalysis/El_Pollo_Loco/2015_URL_Providers"

# Check current working directory.
retval = os.getcwd()
print "Current working directory %s" % retval

# Now change the directory
os.chdir( path )

# Check current working directory.
retval = os.getcwd()

print "Directory changed successfully %s" % retval



#For loop to iterate through the days:
for date in complete_list_of_dates_2015:
	month = date[0]
	day = date[1]
	year = date[2]

	result = []
	f = open('{}_{}_{}_{}_URL_Providers.pickle'.format(company, month, day, year), 'w')
	#What to put in the open() URL area for Chipotle: 'https://www.google.com/#q=Chipotle+news&tbs=cdr%3A1%2Ccd_min%3A{}%2F{}%2F{}%2Ccd_max%3A{}%2F{}%2F{}&tbm='.format(month, day-1, year, month, day, year)
	#for El Pollo Loco: https://www.google.com/#q=el+pollo+loco+news&tbs=cdr%3A%2Ccd_min%3A{}%2F{}%2F{}%2Ccd_max%3A{}%2F{}%2F{}&tbm=
	#For Apple: https://www.google.com/#q=apple+news&tbs=cdr%3A1%2Ccd_min%3A{}%2F{}%2F{}%2Ccd_max%3A{}%2F{}%2F{}&tbm=

	driver.get('https://www.google.com/#q=el+pollo+loco+news&tbs=cdr%3A1%2Ccd_min%3A{}%2F{}%2F{}%2Ccd_max%3A{}%2F{}%2F{}&tbm='.format(month, day-1, year, month, day, year))
	time.sleep(2) #note: month, day, year
	driver.find_elements_by_class_name("crl")
	for res in driver.find_elements_by_class_name('crl'):
		result.append(str(res.text.encode('ascii', 'ignore').decode('ascii')))
	pickle.dump(result, f)
	f.close()




driver.close()




