from pattern.web import *
import pickle

import indicoio
from keys import indico_api_key
indicoio.config.api_key = indico_api_key
company = 'Chevron'
if company in ['El_Pollo_Loco', 'Chipotle']:
	year = '2015'
else:
	year = '2010'


#Loading all the days for naming in the daily_sentiments_function() function
fin = open('list_of_days_{}.pickle'.format(year))
complete_list_of_dates = pickle.load(fin)
fin.close()


def daily_sentiments_function():
	#Changing the directory so that the sentiment pickle file is stored with all the google results 
	import os

	if company in ['El_Pollo_Loco', 'Chipotle']:
		year = '2015'
	else:
		year = '2010'
	print year
	path = "/home/anne/DataAnalysis/{}/{}_Google_Results".format(company, year)
	# Check current working directory.
	retval = os.getcwd()
	print "Current working directory %s" % retval
	# Now change the directory
	os.chdir( path )
	# Check current working directory.
	retval = os.getcwd()
	print "Directory changed successfully %s" % retval

	daily_sentiments_dictionary = {}
	for date in complete_list_of_dates:
		year = date[2]
		month = date[0]
		day = date[1]
		print month, day, year


		#loading the results for interpretation
		fin1 = open('{}_{}_{}googleresults.pickle'.format(month, day, year))
		list_of_results = pickle.load(fin1)
		fin1.close()

		# For storing the sentiments, 
		sentiments = []
		# sentiment_list_length = len(sentiments)

		#looping and appending sentiment results to the list
		for result in list_of_results:
			sentiments.append(indicoio.sentiment(result))
		sentiment_list_length = len(sentiments)


		sentiment_summation = 0

		#finding the average sentiment for this particular day
		x = sentiment_list_length + 1
		denominator_for_averaging = (x + 1) * (x/2)
		for i in range(sentiment_list_length):
			print x
			current_sentiment_weighted_value = x * sentiments[i]
			x -= 1
			print x
			sentiment_summation += current_sentiment_weighted_value
			sentiment_avg = sentiment_summation/denominator_for_averaging
			daily_sentiments_dictionary[month, day, year] = sentiment_avg
	return daily_sentiments_dictionary



dictionary_of_greatness = daily_sentiments_function()

path = "/home/anne/DataAnalysis/Sentiment_Dictionaries"
# Check current working directory.
retval = os.getcwd()
print "Current working directory %s" % retval
# Now change the directory
os.chdir( path )
# Check current working directory.
retval = os.getcwd()
print "Directory changed successfully %s" % retval

f = open('{}_sentiments.pickle'.format(company), 'w')
pickle.dump(dictionary_of_greatness, f)
f.close()