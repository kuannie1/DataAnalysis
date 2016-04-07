from yahoo_finance import Share
from pprint import pprint

def get_stocks(stockName, startDate, endDate):
	company = Share(stockName)
	dates = []
	values = []
	#company.refresh()
	stocks = (company.get_historical(startDate, endDate))
	for item in stocks:
		if 'Date' in item:
			actualDate = item.get('Date')
		if 'Open' in item:
			actualOpen = item.get('Open')
		dates += ([actualDate])
		values += ([actualOpen])

	return dates, values


def get_and_file_save(stockName, startDate, endDate):
	stockInfo = str(get_stocks(stockName, startDate, endDate))
	fileName = 'Company_' + stockName + '_StartOn_' + startDate + '_EndOn_' + endDate
	f = open(fileName, 'w')
	f.write(stockInfo.encode('UTF-8'))
	f.close

Yahoo = 'YHOO'
ElPolloLoco = 'LOCO'
Chipotle = 'CMG'
get_and_file_save(Chipotle, '2015-01-01', '2015-12-31')