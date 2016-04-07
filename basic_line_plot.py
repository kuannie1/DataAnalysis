import numpy as np
import pylab 
import matplotlib.pyplot as plt
from matplotlib.mlab import csv2rec
from matplotlib.cbook import get_sample_data

# # Basic overlayed line graph

import matplotlib.pyplot as plt
plt.plot([5,12,20, 26], [678.40,718.89,670.59,675.00], 'ro', label = 'Stock Price ($)')
plt.plot([5,12,20, 26], [0.8679*500, 0.5698*500,  0.4906*500, 0.6736*500], 'go', label = 'Valuation Based on Public Opinion')
plt.axis([0, 30, 0, 750])
plt.xlabel('Dates in January 2015')
plt.ylabel('Company Valuation')
plt.title('Stock Price v. Public Opinion (Chipotle)')
plt.grid(True)
pylab.legend(loc='lower right')
plt.show()

# 5 12 20 26