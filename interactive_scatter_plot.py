import plotly.plotly as py
import plotly
import plotly.graph_objs as go
import plotly.tools as tls
from yahoo_finance import Share
from pprint import pprint
import pickle
import os
from pattern.web import *
import pickle
import os
from keys import api_username, api_key
tls.set_credentials_file(api_username, api_key)

# USER INPUT REQUIRED
# input string of you ubutu username to define path later
ubuntu_username = 'anne'

# Dictionary that shows user options of company inputs and converts company names to stock names 
company_to_stock = {'El_Pollo_Loco':'LOCO', 'Chipotle':'CMG', 'Valero':'VLO', 'BP':'BP', 'Chevron':'CVX', 'Exxon_Mobil':'XOM'}

# USER INPUT REQUIRED
# input strings of company, start date, and end date of time periodinterested in
company = 'Chevron'
stock = company_to_stock[company]
start_day = '2010-02-02'
end_day = '2010-12-31'

def cursor_labels(company, ubuntu_username):
    """This function takes in a company and the ubuntu user name and returns the labels for the points. 
    This label is a list of strings that include the top headline of Google search results for a specific day
    and the orgainzation that published it.
    """
 
    #The result we want to store:
    cursor_string_list = []

    if company in ['El_Pollo_Loco', 'Chipotle']:
        year = '2015'
    else:
        year = '2010'

    #Get all the days from list_of_days.pickle list:
    fin = open('list_of_days_{}.pickle'.format(year))
    complete_list_of_dates = pickle.load(fin)
    fin.close()
    #For help with indices later:
    num_of_dates = len(complete_list_of_dates)


    path = "/home/{}/DataAnalysis/{}/{}_URL_Providers".format(ubuntu_username, company, year)
    # Check current working directory.
    retval = os.getcwd()
    print "Current working directory %s" % retval
    # Now change the directory
    os.chdir( path )
    # Check current working directory.
    retval = os.getcwd()
    print "Directory changed successfully %s" % retval
    newssource_list = []
    for date in complete_list_of_dates:
        m, d, y = date[0], date[1], date[2]
        f = open('{}_{}_{}_{}_URL_Providers.pickle'.format(company, m, d, y))
        date_newssource_list = pickle.load(f)
        f.close()
        newssource_list.append(date_newssource_list[0])


    path = "/home/{}/DataAnalysis/{}/{}_headlines".format(ubuntu_username, company, year)
    # Checking the current working directory.
    retval = os.getcwd()
    print "Current working directory %s" % retval
    # Now changing the directory
    os.chdir( path )
    # Checking the current working directory.
    retval = os.getcwd()
    print "Directory changed successfully %s" % retval
    
    #Storing the headines in the directory
    headlines_list = []
    for date in complete_list_of_dates:
        m, d, y = date[0], date[1], date[2]
        fin2 = open('{}_{}_{}_{}_headlines.pickle'.format(company, m, d, y))
        date_headlines_list = pickle.load(fin2)
        fin2.close()
        headlines_list.append(date_headlines_list[0])


    path = "/home/{}/DataAnalysis".format(ubuntu_username)
    # Check current working directory.
    retval = os.getcwd()
    print "Current working directory %s" % retval
    # Now change the directory
    os.chdir( path )
    # Check current working directory.
    retval = os.getcwd()
    print "Directory changed successfully %s" % retval

    for i in range(num_of_dates):
        cursor_string_list.append(str(newssource_list[i] + " : " + headlines_list[i]))
    return cursor_string_list

def get_stocks(stockName, startDate, endDate): 
    """ This function takes in a stock name and date range and returns a list of dates and a list of prices.
    The dates need to be formated by 'year-month-day'.
    """
    company = Share(stockName)
    dates = []
    values = []
    stocks = (company.get_historical(startDate, endDate))  # Retreiving the data
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
    """This function uses Plotly's python graphing library to plot an interactive
    graph overlaying the stock data and public opinion values by calling the 
    get_stocks() and get_sentiments() functions for the numerical data and the
    cursor_labels() function for the qualitative data. The function takes a 
    company name, stock name, start date, and end date as inputs."""

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
    # Kernel-style averaging of public opinion values to help visualize clearer trend in public opinion values
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
        text=cursor_labels(companyName, ubuntu_username),
            )

    data = [trace0, trace1]
    layout = go.Layout(
        title=str(company)+' from '+str(startDate) + ' to ' + str(endDate),
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
    # set to plot offline at a local host
    plotly.offline.plot(fig, filename='graval.html')

interactive_scatter_plot(company, stock, start_day, end_day)