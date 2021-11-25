import yfinance as yf
import streamlit as st
import pandas as pd 

st.write("""
    # Simple Stock Price App

    Shown are the stock closing price and volume of Google

    """)
# define ticker symbol for Google
tickerSymbol = 'GOOGL'
# get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
# will provide Open High Low Close volume Dividends Stock Splits information
tickerDf = tickerData.history(period='1d', start='2010-05-31',end='2021-11-24')

st.write('''
## Closing price of Google's Stock
''')

st.line_chart(tickerDf.Close)

st.write('''
## Volume of Google's Stock
''')
st.line_chart(tickerDf.Volume)







