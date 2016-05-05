import plotly.plotly as py
import plotly
import plotly.graph_objs as go
import plotly.tools as tls
from yahoo_finance import Share
from pprint import pprint
from keys import api_username, api_key
tls.set_credentials_file(api_username, api_key)
import pickle
import os
from helperfunctions import *
#DELETE: For your computer path and convenience:
# ubuntu_username = 'udesai'
company_to_stock = {'El_Pollo_Loco':'LOCO', 'Chipotle':'CMG', 'Valero':'VLO', 'BP':'BP', 'Chevron':'CVX', 'Exxon_Mobil':'XOM'}



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

def get_sentiments(companyName, startDate, endDate):
	return combining_everything_together(companyName, startDate, endDate)[1] #sentiment values

def interactive_scatter_plot(companyName, stockName, startDate, endDate):
	list_sentiments_cursor = get_sentiments(companyName, startDate, endDate)
	sentiments = list_sentiments_cursor[1]
	cursor_stuff = get_sentiments[0]

	stock_info = get_stocks(stockName, startDate, endDate)
	trace0 = go.Scatter(
        x = stock_info[0],
        y = stock_info[1],

        mode='lines',
        marker=dict(size=12,
                    line=dict(width=1)
                   ),
        name='Stock Price',
        text=[],
        )
    
    # sentiments = sentiment_info[1]

    # for i in range(2, len(sentiments)-1):
    #     sentiments[i] = (sentiments[i-1] + sentiments[i] + sentiments[i+1])/3
    

    # for i in range(5, len(sentiments)-4):
    #     sentiments[i] = (sentiments[i-4] + sentiments[i-3] + sentiments[i-2] + sentiments[i-1] + sentiments[i] + sentiments[i+1] + sentiments[i+2] + sentiments[i+3] + sentiments[i+4])/9
	trace1 = go.Scatter(
        x = stock_info[0],
        y = sentiments,

        mode='lines',
        marker=dict(size=12,
                    line=dict(width=1)
                   ),
        name='Public Opinion',
        yaxis = 'y2',
        text= cursor_stuff,
            )

	data = [trace0, trace1]
	layout = go.Layout(
        title=str(stockName)+' from '+str(startDate) + ' to ' + str(endDate),
        hovermode='closest',
        xaxis=dict(
            title='Date',
            ticklen=5,
            zeroline=True,
            gridwidth=1,
        ),
        yaxis=dict(
            title='Stock Market Valuation',
            ticklen=5,
            gridwidth=1,
        ),
        yaxis2=dict(
            title = 'Company Popularity',
            ticklen=5,
            gridwidth=1,
            overlaying='y',
            side='right'
            )
    )
	fig = go.Figure(data=data, layout=layout)
	plotly.offline.plot(fig, filename='stockprice_v_publicopinion.html')

company = 'Chipotle'
stock = company_to_stock[company]
start_day = '2015-01-02'
end_day = '2015-12-31'
interactive_scatter_plot(company, stock, start_day, end_day)
#one full year = 127.79 minutes to run! That's like, 2 hours and 8 minutes