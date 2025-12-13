import yfinance as yf
import pandas as pd
import numpy as np

def stock_data(ticker):
    """
    Fetching Real-time data
    """

    try:
        stock = yf.Ticker(ticker)
        #current price
        current_price = stock.history('1d')['Close'].iloc[-1]

        #historical data
        hist = stock.history(period='1y')
        returns = hist['Close'].pct_change().dropna()

        #annualised volatility
        voly = returns.std() * np.sqrt(252)
        #info
        info = stock.info

        return{
            'price': current_price,
            'volatility': voly,
            'name': info.get('longname',ticker),
            'success': True
        }
    except Exception as e:
        return{
            'success': False,
            'error': str(e)
        }
