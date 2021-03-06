## Data Analysis-

### Project Description:
This is a data visualization tool where you can see a company’s stock market and public sentiment values over time. The stock market values were obtained from the Yahoo Finance API. The public sentiment uses Indico’s Public Sentiment API to process Google Search results; the GoogleURL_webscraping.py file takes in the URL search results, depending on the timeframe, and the Indico API evaluates the positivity of those results. 

The interactive_scatter_plot.py file combines everything together, because it takes in the company’s stock name and date range, and, using the Plotly API, plots the stock values, sentiment values, and time in a graph with two y-axes (sentiment and stock prices) and one x-axis (the date range).

### What to install:
We think you have pip installed, but follow these instructions if you don’t. 
Assuming you are running a Linux machine, here are the commands you will need to run in terminal to install all of the packages we will be using to run this program.
$ sudo pip install yahoo-finance
$ sudo pip install plotly

If you are a developer who wants to obtain data for more years, register for a free API key at https://indico.io and type this command in python to test it out:
$ curl 'https://apiv2.indico.io/sentiment?key=yourapikeyhere' --data '{"data": "indico is so easy to use!"}'
Type this command to install the official indicoio API:
$ pip install indicoio

Last but not least, you need to install selenium, an API that has Selenium WebDrivers for accessing information in browsers. 
$ pip install selenium

### How to run file:
Make sure you make a file called keys.py that contains the plotly and indicoio API keys. After that, make a file named .gitignore that has ‘keys.py’ (without the ‘’ marks) in the first line. 

Open interactive_scatter_plot.py. This is the main file that takes an input of a company’s symbol (the letter and number code that denotes the company), start date, and end date and returns an interactive scatter plot that displays the company’s stock market value overlaid with the trend of the public opinion of the company over the specified duration of time. 
An example of the format for calling this function is:

interactive_scatter_plot('LOCO', '2015-01-01', '2015-12-31')

This function call produces a scatterplot comparing the public opinion and stock market values of El Pollo Loco between January 1st and December 31st of 2015. To run interactive_scatter_plot.py scroll to the end of the code and change the interactive_scatter_plot() to contain the company and dates you desire to see the results of. 

There are two different ways to run our code-one with pickle files, and one with real-time calling. 
If you want to customize which company and stock prices you would like to see, use the real-time method where you replace values in the interactive_scatter_plot_take2.py. Unfortunately this method takes a long time. interactive_scatter_plot_take2.py is very inconvenient for a large date range.

Alternatively, you can run interactive_scatter_plot.py, but the options you can pass are restrained. If you input these companies: BP, Valero, Chevron, and Exxon_Mobil, the plot will only display results in the year 2010. If you run these companies: Chipotle and El_Pollo_Loco, you can only get results in the year 2015. This method is a lot faster, because it doesn't have to webcrawl to run. If you use this option, you'll notice that interactive_scatter_plot.py has a variable called "ubuntu_username". Replace "anne" your name or username for your computer, because that variable is essential to finding the files. 

Our website can be found at:
http://kuannie1.github.io/DataAnalysis/
Links to our deliberables can be found here.
