import plotly.plotly as py
import plotly
import plotly.graph_objs as go
import plotly.tools as tls
from yahoo_finance import Share
from pprint import pprint
from keys import api_username, api_key
tls.set_credentials_file(api_username, api_key)
import pickle

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
    #Part 1: Getting the sentiment values for this date range:

    start_y, start_m, start_d = map(int, startDate.split('-'))
    end_y, end_m, end_d = map(int, endDate.split('-'))
    #Reformatting the start & end dates
    formatted_startDate = (start_m, start_d, start_y)
    formatted_endDate = (end_m, end_d, end_y)

    #Get all the days from list_of_days.pickle list:
    fin = open('list_of_days.pickle')
    complete_list_of_dates = pickle.load(fin)
    fin.close()
    #Getting the indexes of the range:
    startdate_index = complete_list_of_dates.index(formatted_startDate)
    enddate_index = complete_list_of_dates.index(formatted_endDate)
    #getting a sliced 
    range_of_dates = complete_list_of_dates[startdate_index:enddate_index + 1]

    f = open('{}_{}_sentiments.pickle'.format(companyName, start_y))
    company_dictionary_of_greatness = pickle.load(f)
    f.close()
    values = [] #sentiment values

    for specific_days in range_of_dates:
        sentiment = company_dictionary_of_greatness[specific_days] #Calling the sentiment for that day
        values.append(sentiment)

    #Part 2: Getting the list of dates the correctly formatted way:
    #Remember: range_of_dates has the range in tuple format
    dates = []
    for date in range_of_dates:
        month = date[0]
        day = date[1]
        year = date[2]
        current_date = '{}-{}-{}'.format(year, month, day)
        dates.append(current_date)

    return dates, values


# print get_sentiments('Chipotle', '2015-1-5', '2015-1-15')


def interactive_scatter_plot(companyName, stockName, startDate, endDate):
    

    stock_info = get_stocks(stockName, startDate, endDate)
    trace0 = go.Scatter(
        x = stock_info[0],
        y = stock_info[1],

        mode='markers',
        marker=dict(size=12,
                    line=dict(width=1)
                   ),
        name='Stock Price',
        text=[],
        )
    sentiment_info = get_sentiments(companyName, startDate, endDate)
    trace1 = go.Scatter(
        x = sentiment_info[0],
        y = sentiment_info[1],

        mode='markers',
        marker=dict(size=12,
                    line=dict(width=1)
                   ),
        name='Public Opinion',
        yaxis = 'y2',
        text=[],
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
