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
company_to_stock = {'El Pollo Loco':'LOCO', 'Chipotle':'CMG', 'Valero':'VLO', 'BP':'BP', 'Chevron':'CVX', 'Exxon Mobil':'XOM'}

def get_stocks(stockName, startDate, endDate): 
    """function that calls the yahoo finance API to get the stock value prices

    input: company stockName, startDate and endDate in 'YYYY-MM-DD' format"""

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
    """
    function that depends on helperfunctions.py script. Returns all the sentiments and all the cursor
    texts in a list like this: [cursortext, sentimentvalues]
    """
    return combining_everything_together(companyName, startDate, endDate) #sentiment values

def interactive_scatter_plot(companyName, stockName, startDate, endDate):
    """
    Takes in values from last two functions and plots the results. 
    """

    list_sentiments_cursor = get_sentiments(companyName, startDate, endDate)
    #sentiment values
    sentiments = list_sentiments_cursor[1]
    #cursor text
    cursor_stuff = list_sentiments_cursor[0]


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

    #Layout, determines features of the graph
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



#Users, plug in values here!
company = 'Chipotle'
stock = company_to_stock[company]
start_day = '2015-01-02'
end_day = '2015-01-09'
interactive_scatter_plot(company, stock, start_day, end_day)