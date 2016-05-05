---
title: Home
layout: template
filename: index
---

# Background:
We chose to combine components of data analytics and visualization to create a tool that visualizes the relationship between a company’s stock price and public opinion (based on top google search results) during a given period of time. This program is designed primarily as a tool that allows the user to easily visualize the connection between interesting events that may have skewed public opinion of a company, such as recent outbreaks of foodborne illness at Chipotle or the BP’s Deepwater Horizon oil spill, and the effect it had on the company’s stock price. This could also be used by investors looking for insight into predictions of a company’s future stock price based on current events or by companies looking to better understand the relationship our tool analyzes.

# Motivations:
Some members wanted to investigate data analytics, while others wanted to focus efforts on data visualization. All members had an interest in analyzing public opinion and its relationship with stock market trends. This project is a way to incorporate both of these areas of interest in an interesting way.

# Assumptions:
- That a company’s stock price is affected by its customers’ positive or negative opinions of them. 
- That the polarity of Google search results for a company can be used as an indicator of that company’s public opinion.
- That the most relevant Google results are at the top. So we utilized a weighting system where we multiply the first sentiment value by 9, the second one by 8, etc., add them up, and divide by 45 (since there are 9 results per page).

# Features:
Our correlation tool produces a graph that overlays a company’s public opinion and stock values on an interactive scatter plot. The x axis represents the time period that the user inputs into our program, the left y axis represents the range of stock values, and the right y axis represents the range of public opinion values. When the user moves the cursor over a data point, they are able to see the numerical value of the data point and, for public opinion values, the top headline of google search results for the company that day. The graph also has zooming, panning, and selecting capabilities that allow the user to zoom in on the information for specific time periods on the graph. All of these features work to help the user draw a connection between events that skewed public opinion of a company and the resulting effect it had on the company’s stock price.

<iframe width="900" height="800" frameborder="0" scrolling="no" src="https://plot.ly/~umadesai/20.embed?autosize=True&link=false&modebar=false&height=450"></iframe>

This is an example of one of the graphs that our tool can output when the inputs ‘Chipotle', ‘2015-02-02', and ‘2015-12-31' are entered into the interactive_scatter_plot.py function as the company name, start date, and end date. 