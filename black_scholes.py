import yfinance as yf
import numpy as np
from scipy.stats import norm

def black_scholes_call(S,K,T,r,sigma):
    """
    Calculate Black-Scholes call option price
    """
    #d1 and d2
    d1 = (np.log(S/K) + (r+0.5*sigma**2)*T)/(sigma*np.sqrt(T))
    d2 = (d1 - sigma*np.sqrt(T))
    call = np.maximum(0,(S*norm.cdf(d1))-(K*np.exp(-r*T)*norm.cdf(d2)))
    return call

def black_scholes_put(S,K,T,r,sigma):
    """
    Calculate Black-Scholes put option price
    """
    #d1 and d2
    d1 = (np.log(S/K) + (r+0.5*sigma**2)*T)/(sigma*np.sqrt(T))
    d2 = (d1 - sigma*np.sqrt(T))
    put = np.maximum(0,(K*np.exp(-r*T)*norm.cdf(-d2))- (S*norm.cdf(-d1)))
    return put

def greeks(S,K,T,r,sigma,optn_type='call'):
    d1 = (np.log(S/K) + (r+0.5*sigma**2)*T)/(sigma*np.sqrt(T))
    d2 = (d1 - sigma*np.sqrt(T))

    #delta
    if optn_type=='call':
        delta = norm.cdf(d1)
    else:
        delta = norm.cdf(d1) - 1
    
    #gamma
    gamma = norm.cdf(d1) / (S*sigma*np.sqrt(T))

    #theta
    if optn_type=='call':
        theta = ((-S*sigma*norm.pdf(d1))/(2*np.sqrt(T))-r*K*np.exp(-r*T)*norm.cdf(d2)) / 365
    else:
        theta = ((-S*sigma*norm.pdf(d1))/(2*np.sqrt(T))+r*K*np.exp(-r*T)*norm.cdf(-d2)) / 365

    #vega
    vega = S * norm.pdf(d1) * np.sqrt(T) / 100
    
    #rho
    if optn_type=='call':
        rho = K * T * np.exp(-r*T) * norm.cdf(d2)
    else:
        rho = -K * T * np.exp(-r*T) * norm.cdf(-d2)

    return{
        'Delta':delta,
        'Gamma':gamma,
        'Theta':theta,
        'Vega':vega,
        'Rho':rho
    }