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

def getting_dates_tuples(startDate, endDate): #date input: yy-mm-dd
	start_y, start_m, start_d = map(int, startDate.split('-'))
	end_y, end_m, end_d = map(int, endDate.split('-'))

    #Reformatting the start & end dates to get tuples:
	formatted_startDate = (start_m, start_d, start_y)
	formatted_endDate = (end_m, end_d, end_y)


    #Getting the indexes of the range:
	startdate_index = final_list_of_dates_2015.index(formatted_startDate)
	enddate_index = final_list_of_dates_2015.index(formatted_endDate)

	#getting a slice
	range_of_dates = final_list_of_dates_2015[startdate_index:enddate_index + 1]
	return range_of_dates


def get_store_googleresults(company, startDate, endDate): #runs google webcrawling for this range
	
	driver = webdriver.Firefox()
	#section 1: getting the link summaries, storing them into one giant list
	list_of_results_lists = [] #1st element contains all results for first day, 2nd element does the same for the 2nd day, etc.
	
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
		result = []
		f = open('{}_{}_{}_{}_googleresults.pickle'.format(company_underscores, month, day, year), 'w')

		driver.get('https://www.google.com/#q={}+news&tbs=cdr%3A1%2Ccd_min%3A{}%2F{}%2F{}%2Ccd_max%3A{}%2F{}%2F{}&tbm='.format(company_plusses, month, day-1, year, month, day, year))
		time.sleep(2) #note: month, day, year
		driver.find_elements_by_class_name('st')
		
		time.sleep(2)

		for res in driver.find_elements_by_class_name('st'):
			result.append(str(res.text.encode('ascii', 'ignore').decode('ascii')))
		list_of_results_lists.append(result)
		pickle.dump(result, f)
	driver.close()
	return list_of_results_lists 

def get_store_headlines(company, startDate, endDate): #runs google webcrawling for this range
	driver = webdriver.Firefox()
	
	#section 1: getting the link summaries, storing them into one giant list
	list_of_headlines_lists = [] #1st element contains all results for first day, 2nd element does the same for the 2nd day, etc.
	
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
		result = []
		f = open('{}_{}_{}_{}_googleheadlines.pickle'.format(company_underscores, month, day, year), 'w')

		driver.get('https://www.google.com/#q={}+news&tbs=cdr%3A1%2Ccd_min%3A{}%2F{}%2F{}%2Ccd_max%3A{}%2F{}%2F{}&tbm='.format(company_plusses, month, day-1, year, month, day, year))
		time.sleep(2) #note: month, day, year
		driver.find_elements_by_class_name('r')
		
		time.sleep(2)

		for res in driver.find_elements_by_class_name('r'):
			one_headline = str(res.text.encode('ascii', 'ignore').decode('ascii'))
			result.append(one_headline)
		list_of_headlines_lists.append(result)
		pickle.dump(result, f)
	driver.close()
	return list_of_headlines_lists

def get_store_sponsors(company, startDate, endDate): #runs google webcrawling for this range
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
		result = []
		f = open('{}_{}_{}_{}_googlesponsors.pickle'.format(company_underscores, month, day, year), 'w')

		driver.get('https://www.google.com/#q={}+news&tbs=cdr%3A1%2Ccd_min%3A{}%2F{}%2F{}%2Ccd_max%3A{}%2F{}%2F{}&tbm='.format(company_plusses, month, day-1, year, month, day, year))
		time.sleep(2) #note: month, day, year
		driver.find_elements_by_class_name('crl')
		
		time.sleep(2)

		for res in driver.find_elements_by_class_name('crl'):
			one_sponsor = str(res.text.encode('ascii', 'ignore').decode('ascii'))
			if one_sponsor == "":
				pass
			else:
				result.append(one_sponsor)
		list_of_sponsors_lists.append(result)
		pickle.dump(result, f)
	driver.close()
	return list_of_sponsors_lists

def combine_header_and_sponsors(company, startDate, endDate):
	sponsors_list = get_store_sponsors(company, startDate, endDate)
	headline_list = get_store_headlines(company, startDate, endDate)
	changing_value = 0
	combined_result = []
	for element in sponsors_list:
		final_string = element[0] + " : " + headline_list[changing_value][0]
		changing_value += 1
		combined_result.append(final_string)
	return combined_result

# print combine_header_and_sponsors('El Pollo Loco', '2015-02-02', '2015-02-05')

def find_sentiment_values(company, startDate, endDate):
	daily_google_results = get_store_googleresults(company, startDate, endDate) #represents a list of lists
	# print daily_google_results
	overall_value_list = [] #list of multiple daily_value_list (s)

	for day_results in daily_google_results:
		total_num_descriptions = len(daily_google_results[0]) - 1
		updating_value = 0 #will help with incrementing up
		daily_value_list = [] #sentiment values for one day, placed here because I want it to reset
		for individual_result in day_results:
			num = indicoio.sentiment(individual_result) * total_num_descriptions
			updating_value += 1
			total_num_descriptions -= 1
			daily_value_list.append(num)
		overall_value_list.append(daily_value_list)
	final_sentiment_list = []
	for a_list in overall_value_list:
		summation = 0
		for weighted_sentiment in a_list:
			summation += weighted_sentiment
		final_average_for_day = summation / 45
		final_sentiment_list.append(final_average_for_day)
	return final_sentiment_list

	return overall_value_list

# print find_sentiment_values('Apple', '2015-02-02', '2015-02-05')


def removing_files_created(company, startDate, endDate):
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
	# removing
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
	#hopefully datelist is already made by calling functions!! *crosses fingers*
	for_the_cursors = combine_header_and_sponsors(company, startDate, endDate)
	for_the_points = find_sentiment_values(company, startDate, endDate)
	removing_files_created(company, startDate, endDate)

	return [for_the_cursors, for_the_points] #returning a list because tuples are annoying


# print combining_everything_together('Chipotle', '2015-02-02', '2015-02-05')



