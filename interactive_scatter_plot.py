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
from BP_headline_provider_script import BP_cursor_string_list
#For your computer path and convenience:
ubuntu_username = 'udesai'
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
    #Changing the directory so that the sentiment pickle file is stored with all the google results 
    import os
    path = "/home/{}/DataAnalysis/Sentiment_Dictionaries".format(ubuntu_username)
    # Check current working directory.
    retval = os.getcwd()
    print "Current working directory %s" % retval
    # Now change the directory
    os.chdir( path )
    # Check current working directory.
    retval = os.getcwd()
    print "Directory changed successfully %s" % retval

    start_y, start_m, start_d = map(int, startDate.split('-'))
    end_y, end_m, end_d = map(int, endDate.split('-'))
    #Reformatting the start & end dates
    formatted_startDate = (start_m, start_d, start_y)
    formatted_endDate = (end_m, end_d, end_y)

    #Get all the days from list_of_days.pickle list:
    fin = open('list_of_days_{}.pickle'.format(start_y))
    complete_list_of_dates = pickle.load(fin)
    fin.close()
    #Getting the indexes of the range:
    startdate_index = complete_list_of_dates.index(formatted_startDate)
    enddate_index = complete_list_of_dates.index(formatted_endDate)
    #getting a sliced 
    range_of_dates = complete_list_of_dates[startdate_index:enddate_index + 1]

    f = open('{}_{}_sentiments.pickle'.format(companyName, start_y))
    # f = open('{}_headlines_sentiments.pickle'.format(companyName))
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


#changing the directory back to normal:
path = "/home/{}/DataAnalysis".format(ubuntu_username)
# Check current working directory.
retval = os.getcwd()
print "Current working directory %s" % retval
# Now change the directory
os.chdir( path )
# Check current working directory.
retval = os.getcwd()
print "Directory changed successfully %s" % retval


def interactive_scatter_plot(companyName, stockName, startDate, endDate):

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
    sentiment_info = get_sentiments(companyName, startDate, endDate)
    sentiments = sentiment_info[1]
    # for i in range(2, len(sentiments)-1):
    #     sentiments[i] = (sentiments[i-1] + sentiments[i] + sentiments[i+1])/3
    for i in range(5, len(sentiments)-4):
        sentiments[i] = (sentiments[i-4] + sentiments[i-3] + sentiments[i-2] + sentiments[i-1] + sentiments[i] + sentiments[i+1] + sentiments[i+2] + sentiments[i+3] + sentiments[i+4])/9
    trace1 = go.Scatter(
        x = sentiment_info[0],
        y = sentiments,

        mode='lines',
        marker=dict(size=12,
                    line=dict(width=1)
                   ),
        name='Public Opinion',
        yaxis = 'y2',
        text=BP_cursor_string_list,
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

company = 'BP'
stock = company_to_stock[company]
start_day = '2010-02-02'
end_day = '2010-12-31'
interactive_scatter_plot(company, stock, start_day, end_day)
