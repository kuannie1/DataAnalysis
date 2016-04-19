from pattern.web import *
import pickle

import indicoio
from keys import indico_api_key
indicoio.config.api_key = indico_api_key


#Loading all the days for naming in the daily_sentiments_function() function
fin = open('list_of_days.pickle')
complete_list_of_dates = pickle.load(fin)
fin.close()
#Changing the directory so that the sentiment pickle file is stored with all the google results 
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

def daily_sentiments_function():
	"""
	"""
	daily_sentiments_dictionary = {}
	for date in complete_list_of_dates:
		year = date[2]
		month = date[0]
		day = date[1]

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
		for i in range(sentiment_list_length):
			sentiment_summation += sentiments[i]
			sentiment_avg = sentiment_summation/sentiment_list_length
			daily_sentiments_dictionary[month, day, year] = sentiment_avg
	return daily_sentiments_dictionary

dictionary_of_greatness = daily_sentiments_function()
f = open('sentiments.pickle', 'w')
pickle.dump(dictionary_of_greatness, f)
f.close()

	#Create dictionary with date leading to sentiment


# f = open('{}_sentiments.pickle'.format(month), 'w')
# pickle.dump(daily_sentiments(), f)
# f.close()



#Indicoio examples:
	# print "The Average Sentiment value for day {} is: ".format(day) + str(sentiment_avg)


# # single example
# print indicoio.sentiment("I love writing code!")

