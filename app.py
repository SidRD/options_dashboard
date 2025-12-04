import streamlit as st
import numpy as np
from black_scholes import black_scholes_call, black_scholes_put, greeks

#Page config
st.set_page_config('Option Pricing Dashboard')
st.title('Black-Scholes Option Pricing Dashboard')

st.sidebar.header('Option Parameters')

#input widgets
S = st.sidebar.number_input('Stock Price ($)', min_value=0.01, value=10.0)
K = st.sidebar.number_input('Strike Price ($)', min_value=0.01, value=10.0, step=5.0)
T = st.sidebar.number_input('Time to expiration (Years)', min_value=0.000, value=0.2500)
r = st.sidebar.slider('Risk-Free Rate(%)',0,50,4) / 100
sigma = st.sidebar.slider('Volatility (%)', 0, 100,10) /100

callp = black_scholes_call(S,K,T,r,sigma)
putp = black_scholes_put(S,K,T,r,sigma)

#display
st.header('Option Prices')
col1, col2 = st.columns(2)

with col1:
    st.metric('Call Option',f'${callp:.3f}')
with col2:
    st.metric('Put Option',f'${putp:.3f}')

#greeks
st.header('Option Greeks')
c_greeks = greeks(S,K,T,r,sigma,'call')
p_greeks = greeks(S,K,T,r,sigma,'put')

col1, col2 = st.columns(2)

with col1:
    st.subheader("Call Greeks")
    st.write(f"Delta: {c_greeks['Delta']:.3f}")
    st.write(f"Gamma: {c_greeks['Gamma']:.3f}")
    st.write(f"Theta: {c_greeks['Theta']:.3f}")
    st.write(f"Vega: {c_greeks['Vega']:.3f}")
    st.write(f"Rho: {c_greeks['Rho']:.3f}")

with col2:
    st.subheader("Put Greeks")
    st.write(f"Delta: {p_greeks['Delta']:.3f}")
    st.write(f"Gamma: {p_greeks['Gamma']:.3f}")
    st.write(f"Theta: {p_greeks['Theta']:.3f}")
    st.write(f"Vega: {p_greeks['Vega']:.3f}")
    st.write(f"Rho: {p_greeks['Rho']:.3f}")