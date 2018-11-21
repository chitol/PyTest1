import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

start =dt.datetime(2018,1,18)
end =dt.datetime(2018,11,18)

df = web.DataReader('QCOM', 'yahoo', start, end)
#df.to_csv('mycsv.csv')
#print(df.head(9))


#df = pd.read_csv('mycsv.csv', parse_dates=True, index_col=0)
print(df[['Open','High']].head())

#df['Adj Close'].plot()
df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()

#print(df.tail(50))

ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=5, colspan=1)

ax1.plot(df.index, df['Adj Close'])
ax1.plot(df.index, df['100ma'])

ax2.bar(df.index, df['Volume'])
plt.show()