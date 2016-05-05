## This file is not currently being used for anything.
# The same function "get_stocks()" is in the code that creates the plot to decrease run time.

from yahoo_finance import Share
from pprint import pprint

def get_stocks(stockName, startDate, endDate):
	""" This function takes in a stock name and date range and returns a list of dates and a list of prices
	The dates need to be formated by 'year-month-day' 
	"""
	company = Share(stockName)
	dates = []
	values = []
	#company.refresh()
	stocks = (company.get_historical(startDate, endDate))  # Retreiving the data
	for item in stocks:
		if 'Date' in item:
			actualDate = item.get('Date')
		if 'Open' in item:
			actualOpen = item.get('Open')
		dates += ([actualDate])
		values += ([actualOpen])

	return dates, values


def get_and_file_save(stockName, startDate, endDate):
	""" This calls get_stocks() and returns the result into a file"""
	stockInfo = str(get_stocks(stockName, startDate, endDate))
	fileName = 'Company_' + stockName + '_StartOn_' + startDate + '_EndOn_' + endDate
	f = open(fileName, 'w')
	f.write(stockInfo.encode('UTF-8'))
	f.close

Yahoo = 'YHOO'
ElPolloLoco = 'LOCO'
Chipotle = 'CMG'
get_and_file_save(Chipotle, '2015-01-01', '2015-12-31')