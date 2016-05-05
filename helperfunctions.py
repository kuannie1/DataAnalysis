from datetime import datetime, time
from pattern.web import * 
from pattern.web import URL, extension, download
import pickle as pickle
from selenium import webdriver
from customdates2 import final_list_of_dates_2010, final_list_of_dates_2011, final_list_of_dates_2012, final_list_of_dates_2013, final_list_of_dates_2014, final_list_of_dates_2015
import os, sys
import indicoio
from keys import indico_api_key
indicoio.config.api_key = indico_api_key


# stock_open is a list that has all the days the stock market is open. 
# Each day is in tuple form (mm, dd, yyyy) for our assigning convenience
stock_open = []
list_of_lists_dates = [final_list_of_dates_2010, final_list_of_dates_2011, final_list_of_dates_2012, final_list_of_dates_2013, final_list_of_dates_2014, final_list_of_dates_2015]

for year in list_of_lists_dates:
	#Loops through each year
	for day in year:
		#Loops through each day in the year
		stock_open.append(day)


def getting_dates_tuples(startDate, endDate): #date input: yy-mm-dd
	""" 
	Takes in the startDate and endDate in the despicable format 'yyyy-mm-dd'
	Converts those dates to the nice tuple format (mm, dd, yyyy) 
	and stores those values in variables: start_y, end_y, start_m, end_m, and start_d, end_d

	Gets a list containing the startDate, endDate, and every date in between

	Function is important because next few functions rely on a list of dates with this format
	"""
	start_y, start_m, start_d = map(int, startDate.split('-'))
	end_y, end_m, end_d = map(int, endDate.split('-'))

    #Reformatting the start & end dates to get tuples:
	formatted_startDate = (start_m, start_d, start_y)
	formatted_endDate = (end_m, end_d, end_y)


    #Getting the indexes of the start & end dates--helpful for list slicing
	startdate_index = stock_open.index(formatted_startDate)
	enddate_index = stock_open.index(formatted_endDate)

	#getting a slice of the biggest list of dates we have
	range_of_dates = stock_open[startdate_index:enddate_index + 1]
	return range_of_dates


def get_store_googleresults(company, startDate, endDate): #runs google webcrawling for this range
	
	"""
	Gets all the google results for one company by webcrawling
	# of results depend on the number of days between the startDate, and endDate
	Although this f(x) stores the results, it returns the contents of all of those files in one list
	"""


	driver = webdriver.Firefox() #Opening FireFox window, start of webcrawling
	
	#1st element contains all results for first day, 2nd element does the same for the 2nd day, etc.
	list_of_results_lists = [] 


	#Making naming easier:
	company_plusses = "" #for google result convenience
	company_underscores = "" # for file naming convenience
	
	if " " in company: #the loop that helps make company_plusses & company_underscores
		for char in company:
			if char != " ":
				company_plusses += char
				company_underscores += char
			else:
				company_plusses += "+"
				company_underscores += "_"
	else:
		company_plusses = company
		company_underscores = company
	
	#Iterating through the days:
	datelist = getting_dates_tuples(startDate, endDate)
	for date in datelist:
		month = date[0]
		day = date[1]
		year = date[2]

		# print month, day, year #command for debugging what dates don't work out

		# result is supposed to have all the link summaries in one list, 
		#supposed to reset with each new date
		result = []

		#formatting file name to automatically store these google results in an understandable way
		f = open('{}_{}_{}_{}_googleresults.pickle'.format(company_underscores, month, day, year), 'w')
		driver.get('https://www.google.com/#q={}+news&tbs=cdr%3A1%2Ccd_min%3A{}%2F{}%2F{}%2Ccd_max%3A{}%2F{}%2F{}&tbm='.format(company_plusses, month, day-1, year, month, day, year))
		time.sleep(2) #note: month, day, year
		driver.find_elements_by_class_name('st')
		# time.sleep(2)

		#Appending each google result to the list
		for res in driver.find_elements_by_class_name('st'):
			result.append(str(res.text.encode('ascii', 'ignore').decode('ascii')))
		list_of_results_lists.append(result)
		pickle.dump(result, f)

	driver.close()

	print "All link summaries are stored"
	#Like we mentioned before:
	#1st element contains all results for first day, 2nd element does the same for the 2nd day, etc.
	return list_of_results_lists 

def get_store_headlines(company, startDate, endDate): #runs google webcrawling for this range
	
	"""
	Gets all the google link headlines for one company by webcrawling
	# of results depend on the number of days between the startDate, and endDate
	Although this f(x) stores the headlines, it returns the contents of all of those files in one list
	"""	

	driver = webdriver.Firefox()#Opening FireFox window, start of webcrawling
	
	list_of_headlines_lists = [] #1st element contains all headlines for first day, 2nd element does the same for the 2nd day, etc.
	

	#if there are spaces in the company name:
	datelist = getting_dates_tuples(startDate, endDate)
	company_plusses = "" #for google-result substitution convenience
	company_underscores = "" # for file-naming convenience
	
	#Making naming easier:
	if " " in company: #the loop that helps make company_plusses & company_underscores
		for char in company:
			if char != " ":
				company_plusses += char
				company_underscores += char
			else:
				company_plusses += "+"
				company_underscores += "_"
	else:
		company_plusses = company
		company_underscores = company
	
	#iterate through the days:
	for date in datelist:
		month = date[0]
		day = date[1]
		year = date[2]

		# print month, day, year #For debugging purposes, seeing which days don't work

		# result is supposed to have all the link summaries in one list, 
		# supposed to reset with each new date
		result = []

		#formatting file name to automatically store these google results in an understandable way
		f = open('{}_{}_{}_{}_googleheadlines.pickle'.format(company_underscores, month, day, year), 'w')

		driver.get('https://www.google.com/#q={}+news&tbs=cdr%3A1%2Ccd_min%3A{}%2F{}%2F{}%2Ccd_max%3A{}%2F{}%2F{}&tbm='.format(company_plusses, month, day-1, year, month, day, year))
		time.sleep(2) #note: month, day, year
		driver.find_elements_by_class_name('r') #The headline class, from looking at the source code from a google search result page

		for res in driver.find_elements_by_class_name('r'):
			one_headline = str(res.text.encode('ascii', 'ignore').decode('ascii'))
			result.append(one_headline)
		list_of_headlines_lists.append(result)
		pickle.dump(result, f)
	driver.close()

	print "All headlines are stored"
	#Like what we mentioned before:
	#1st element contains all headlines for first day, 2nd element does the same for the 2nd day, etc.
	return list_of_headlines_lists




def get_store_sponsors(company, startDate, endDate): #runs google webcrawling for this range
	
	"""
	Gets all the google link sponsors for one company by webcrawling
	# of results depend on the number of days between the startDate, and endDate
	Although this f(x) stores the sponsors, it returns the contents of all of those files in one list
	"""	

	driver = webdriver.Firefox()
	
	#section 1: getting the link summaries, storing them into one giant list
	list_of_sponsors_lists = [] #1st element contains all results for first day, 2nd element does the same for the 2nd day, etc.
	
	#if there are spaces in the company name:
	datelist = getting_dates_tuples(startDate, endDate)
	company_plusses = "" #for google result convenience
	company_underscores = "" # for file naming convenience
	
	if " " in company: #the loop that helps make company_plusses & company_underscores
		for char in company:
			if char != " ":
				company_plusses += char
				company_underscores += char
			else:
				company_plusses += "+"
				company_underscores += "_"
	else:
		company_plusses = company
		company_underscores = company
	
	#For loop to iterate through the days:
	for date in datelist:
		month = date[0]
		day = date[1]
		year = date[2]

		# print month, day, year

		#result is a list that contains all the link sponsors for that day
		#starts blank because we want to reset it for every day
		result = []

		#the next few lines repeat principles from the previous functions
		#see previous functions
		f = open('{}_{}_{}_{}_googlesponsors.pickle'.format(company_underscores, month, day, year), 'w')

		driver.get('https://www.google.com/#q={}+news&tbs=cdr%3A1%2Ccd_min%3A{}%2F{}%2F{}%2Ccd_max%3A{}%2F{}%2F{}&tbm='.format(company_plusses, month, day-1, year, month, day, year))
		time.sleep(2) #note: month, day, year
		driver.find_elements_by_class_name('crl')#The link sponsors class, from looking at the source code from a google search result page

		
		# time.sleep(2)

		for res in driver.find_elements_by_class_name('crl'):
			one_sponsor = str(res.text.encode('ascii', 'ignore').decode('ascii'))
			#supposed to skip over websites with no sponsors
			if one_sponsor == "":
				pass
			else:
				result.append(one_sponsor)

		list_of_sponsors_lists.append(result)
		pickle.dump(result, f)
	driver.close()


	print "All sponsors are stored"

	#note: unlike previous lists, not every list/element has length 10
	return list_of_sponsors_lists

def combine_header_and_sponsors(company, startDate, endDate):
	"""
	Makes a list of strings. Each string is formatted like this:
	["1st sponsor : 1st headline" (or 0th), "2nd sponsor : 2nd headline", "3rd sponsor : 3rd headline", ... "nth sponsor : nth headline"]
	"""
	#next 2 lines rely on functions in previous lines:
	sponsors_list = get_store_sponsors(company, startDate, endDate)
	headline_list = get_store_headlines(company, startDate, endDate)

	#For incrementing sake, since we want to get all the days in the sponsors_list and headline_list
	changing_value = 0

	#The final result we want to return, look at docstring
	combined_result = []
	#Looping to get the 1st element of each entry of both lists
	for element in sponsors_list:
		final_string = element[0] + " : " + headline_list[changing_value][0]
		changing_value += 1
		combined_result.append(final_string)
	
	print "The sponsor:headline links have been created"

	return combined_result

# example command:
# print combine_header_and_sponsors('El Pollo Loco', '2015-02-02', '2015-02-05')

def find_sentiment_values(company, startDate, endDate):
	"""
	Takes in the company name, start date, and end date. 
	Looks into the pickle file and runs sentiment analysis on each entry.

	Weights those sentiment values that places more emphasis on the 1st few entries
	Assigns a list of those results to a variable(final_sentiment_list), and returns that variable
	"""
	#since we're calling get_store_googleresults(), 
	#we don't need to run getting_date_tuples() because get_store_googleresults() 
	#already calls that function
	#daily_google_results gets the gigantic list generated by get_store_googleresults()
	#reminder that list represents list of lists with each entry representing 
	#a day's worth of google results
	daily_google_results = get_store_googleresults(company, startDate, endDate)
	
	# for debugging, so we can double check that the text matches with URL's results
	# print daily_google_results
	
	#list of multiple daily_value_list(s, plural)
	overall_value_list = [] 
	for day_results in daily_google_results:

		#For incrementing purposes, assigned here because it should reset for each day
		total_num_descriptions = len(daily_google_results[0]) - 1 
		updating_value = 0 

		#sentiment values for one day, placed here because I want it to reset
		daily_value_list = [] 

		#Looping to store these sentiment values, 
		#using a weighting system that's dependent on total_num_descriptions
		#updating_value may be unnecessary, but helpful for us to store & see
		for individual_result in day_results:
			num = indicoio.sentiment(individual_result) * total_num_descriptions
			updating_value += 1
			total_num_descriptions -= 1
			daily_value_list.append(num)

		overall_value_list.append(daily_value_list)
	

	#final_sentiment_is a list that has a sentiment value for each day-index
	final_sentiment_list = []

	#The loop for averaging all the values for one day. 
	for a_list in overall_value_list:
		summation = 0
		for weighted_sentiment in a_list:

			summation += weighted_sentiment
		final_average_for_day = summation / 45 
		#note: 45 represents the # of results if there were 9 of the 1st google result, 8 of the 2nd google result, etc.
		
		final_sentiment_list.append(final_average_for_day)
	return final_sentiment_list

# print find_sentiment_values('Apple', '2015-02-02', '2015-02-05')


def removing_files_created(company, startDate, endDate):
	"""
	Deleting the pickle files, since they're not needed anymore. 
	Doesn't return anything.
	"""
	company_underscores = "" # for file naming convenience
	
	if " " in company: #the loop that helps make company_plusses & company_underscores
		for char in company:
			if char != " ":
				company_underscores += char
			else:
				company_underscores += "_"
	else:
		company_underscores = company

	# listing directories
	# print "The dir is: %s" %os.listdir(os.getcwd())  #print statement to debug, if we accidentally delete everything
	datelist = getting_dates_tuples(startDate, endDate)
	# loop for removing
	for date in datelist:
		month = date[0]
		day = date[1] 
		year = date[2]
		#For checking to see if the file is there:
		if os.path.isfile("{}_{}_{}_{}_googleresults.pickle".format(company_underscores, month, day, year)):
			os.remove("{}_{}_{}_{}_googleresults.pickle".format(company_underscores, month, day, year))
		if os.path.isfile("{}_{}_{}_{}_googlesponsors.pickle".format(company_underscores, month, day, year)):
			os.remove("{}_{}_{}_{}_googlesponsors.pickle".format(company_underscores, month, day, year))
		if os.path.isfile("{}_{}_{}_{}_googleheadlines.pickle".format(company_underscores, month, day, year)):
			os.remove("{}_{}_{}_{}_googleheadlines.pickle".format(company_underscores, month, day, year))

	# listing directories after removing path
	# print "The dir after removal of path : %s" %os.listdir(os.getcwd()) #print statement to debug, if we accidentally delete everything


def combining_everything_together(company, startDate, endDate):
	"""
	Calls the combine_header_and_sponsors(), find_sentiment_values(), and removing_files_created()
	functions to get inputs needed for the interactive scatter plot code. 
	"""

	#hopefully datelist is already made by calling functions!! *crosses fingers*
	for_the_cursors = combine_header_and_sponsors(company, startDate, endDate)
	for_the_points = find_sentiment_values(company, startDate, endDate)
	removing_files_created(company, startDate, endDate)
	public_ops = [for_the_cursors, for_the_points] 
	return public_ops #returning a list because tuples are annoying


# print combining_everything_together('Chipotle', '2015-02-02', '2015-02-05')



