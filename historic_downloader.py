#Historic Downloader
import yfinance as yf
import matplotlib.pyplot as plt
import sys
import pandas

data = yf.download(tickers=['BTC-USD'], period="max", interval="5m")
# Plot the close prices
data.Close.plot()
plt.show()

data.to_csv("test.csv")
sys.exit()