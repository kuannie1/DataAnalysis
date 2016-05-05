---
title: Home
layout: template
filename: index
---

# Background:
We chose to combine components of data analytics and visualization to create a tool that visualizes the relationship between a company’s stock price and public opinion (based on top google search results) during a given period of time. This program is designed primarily as a tool that allows the user to easily visualize the connection between interesting events that may have skewed public opinion of a company, such as recent outbreaks of foodborne illness at Chipotle or the BP’s Deepwater Horizon oil spill, and the effect it had on the company’s stock price. This could also be used by investors looking for insight into predictions of a company’s future stock price based on current events or by companies looking to better understand the relationship our tool analyzes.

# Assumptions:
- That a company’s stock price is affected by its customers’ positive or negative opinions of them. 
- That the polarity of Google search results for a company can be used as an indicator of that company’s public opinion.
- That the most relevant Google results are at the top. So we utilized a weighting system where we multiply the first sentiment value by 9, the second one by 8, etc., add them up, and divide by 45 (since there are 9 results per page).