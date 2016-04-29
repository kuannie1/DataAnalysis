from pattern.web import *
import pickle

import indicoio
from keys import indico_api_key
indicoio.config.api_key = indico_api_key
import os



company = 'Chevron'
ubuntu_username = 'anne'
#The result we want to store:
BP_cursor_string_list = []

if company in ['El_Pollo_Loco', 'Chipotle']:
	year = '2015'
else:
	year = '2010'

#Get all the days from list_of_days.pickle list:
fin = open('list_of_days_{}.pickle'.format(year))
complete_list_of_dates = pickle.load(fin)
fin.close()
#For help with indices later:
num_of_dates = len(complete_list_of_dates)



path = "/home/{}/DataAnalysis/{}/{}_URL_Providers".format(ubuntu_username, company, year)
# Check current working directory.
retval = os.getcwd()
print "Current working directory %s" % retval
# Now change the directory
os.chdir( path )
# Check current working directory.
retval = os.getcwd()
print "Directory changed successfully %s" % retval
newssource_list = []
for date in complete_list_of_dates:
	m, d, y = date[0], date[1], date[2]
	f = open('{}_{}_{}_{}_URL_Providers.pickle'.format(company, m, d, y))
	date_newssource_list = pickle.load(f)
	f.close()
	newssource_list.append(date_newssource_list[0])




path = "/home/{}/DataAnalysis/{}/{}_headlines".format(ubuntu_username, company, year)
# Check current working directory.
retval = os.getcwd()
print "Current working directory %s" % retval
# Now change the directory
os.chdir( path )
# Check current working directory.
retval = os.getcwd()
print "Directory changed successfully %s" % retval


headlines_list = []
for date in complete_list_of_dates:
	m, d, y = date[0], date[1], date[2]
	fin2 = open('{}_{}_{}_{}_headlines.pickle'.format(company, m, d, y))
	date_headlines_list = pickle.load(fin2)
	fin2.close()
	headlines_list.append(date_headlines_list[0])

# print headlines_list


path = "/home/{}/DataAnalysis".format(ubuntu_username)
# Check current working directory.
retval = os.getcwd()
print "Current working directory %s" % retval
# Now change the directory
os.chdir( path )
# Check current working directory.
retval = os.getcwd()
print "Directory changed successfully %s" % retval



for i in range(num_of_dates):
	BP_cursor_string_list.append(str(newssource_list[i] + " : " + headlines_list[i]))


print BP_cursor_string_list


