from pattern.web import *
import pickle

import indicoio
from keys import indico_api_key
indicoio.config.api_key = indico_api_key


Jan_days = [2, 5, 6, 7, 8, 9, 12, 13, 14, 15, 16, 19, 20, 21, 22, 23, 26, 27, 28, 29, 30]

def January_sentiments():
	daily_sentiments = []
	for day in Jan_days:
		#loading the results for interpretation
		fin = open('Jan{}_results.pickle'.format(day))
		result_list = pickle.load(fin)
		fin.close()

		# For storing the sentiments, 
		sentiments = []
		sentiment_list_length = len(sentiments)

		#looping and appending sentiment results to the list
		for result in result_list:
			sentiments.append(indicoio.sentiment(result))
		sentiment_list_length = len(sentiments)

		sentiment_summation = 0
		#finding the average sentiment for this particular day
		for i in range(sentiment_list_length):
			sentiment_summation += sentiments[i]
			sentiment_avg = sentiment_summation/ sentiment_list_length
		daily_sentiments.append(sentiment_avg)

	return daily_sentiments #the list, with one sentiment value/day

print January_sentiments()
		


	# print "The Average Sentiment value for day {} is: ".format(day) + str(sentiment_avg)


# # single example
# print indicoio.sentiment("I love writing code!")

