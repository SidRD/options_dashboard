from black_scholes import black_scholes_call, black_scholes_put

S = 100    # Stock price
K = 105    # Strike price
T = 0.25   # 3 months
r = 0.05   # 5% interest rate
sigma = 0.20  # 20% volatility

call, put = black_scholes_call(S,K,T,r,sigma), black_scholes_put(S,K,T,r,sigma)

print(f'Call option price is ${call:.2f} \nPut option price is ${put:.2f}')
