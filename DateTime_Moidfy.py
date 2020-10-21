"""

https://machinelearningmastery.com/resample-interpolate-time-series-data-python/
Example-01
Suppose the data is not having any year and the data is only in the form of the months the following can help in formatting.

""

from pandas import read_csv
from pandas import datetime
from matplotlib import pyplot

def parser(x):
  return datetime.strptime('190'+x,'%Y-%m')
  
series=read_csv('data.csv',header=0,parser_dates=[0],index_col=0, squeeze=True, date_parser=parser)
print(series.head())
series.plot()
pyplot.show()



