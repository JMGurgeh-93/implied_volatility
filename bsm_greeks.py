# calculating the 'Greeks' 

import bsm_model # importing the model we built in bsm model
import math
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

S = 100.0   # price of the underlying
K = 110.0   # strike price
T = 0.8     # time to maturity in years
r = 0.05    # annualised risk-free rate
sigma = 0.2 # realised volatility 
q = 0.0     # the dividend yield 
ds = 1e-5   # the increment in stock price that we use for differentiation

def d1(S, K, T, r, sigma):
    return (np.log(S/K) + (r + sigma**2/2)*T) /\
                     (sigma*np.sqrt(T))

def d2(S, K, T, r, sigma):
    return d1(S, K, T, r, sigma) - sigma* np.sqrt(T)

def delta_call(S, K, T, r, sigma):
    N = norm.cdf
    return N(d1(S, K, T, r, sigma))

def delta_put(S, K, T, r, sigma):
    N = norm.cdf
    return -N(-d1(S, K, T, r, sigma))

def delta_fdm_call(S, K, T, r, sigma, q, ds):
    return (bsm_model.our_call(S + ds, K, T, r, sigma, q) - 
            bsm_model.our_call(S, K, T, r, sigma, q))/ds

def delta_fdm_put(S, K, T, r, sigma, q, ds):
    return (bsm_model.our_put(S + ds, K, T, r, sigma, q) - 
            bsm_model.our_put(S, K, T, r, sigma, q))/ds

# using arange to generate a set of prices against which we can plot the delta
prices = np.arange(1, 300, 1)
deltas_call = delta_call(prices, K, T, r, sigma)
deltas_put = delta_put(prices, K, T, r, sigma)
deltas_fdm_call = delta_fdm_call(prices, K, T,r, sigma, q, ds)
deltas_fdm_put = delta_fdm_put(prices, K, T,r, sigma, q, ds)

plt.style.use("seaborn-v0_8-darkgrid")
plt.figure(1)
plt.plot(prices, deltas_call, label = 'Call Delta')
plt.plot(prices, deltas_put, label = 'Put Delta')
plt.xlabel('$S_0$')
plt.ylabel('Delta')
plt.title('Effect of underlying stock price on option delta')
plt.axvline(K, color='black', linestyle='dashed', linewidth=2,label="Strike")
plt.legend()
plt.show(block = False)

# looking at the error between the analytical and numerical methods
call_error = np.array(deltas_call) - np.array(deltas_fdm_call)
put_error = np.array(deltas_put) - np.array(deltas_fdm_put)

plt.figure(2)
plt.plot(prices, call_error, label = 'Call method errors')
plt.plot(prices, put_error, label = 'Put method errors')
plt.legend()
plt.xlabel('$S_0$')
plt.ylabel('FDM Error')
plt.show()