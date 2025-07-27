"""A simple attempt to model the Black-Scholes equation for calculating options
prices in python"""

import math 
import numpy as np
from scipy.stats import norm
import blackscholes as bsm_ref # reference function to check our model

# writing out the main BSM function

def bsm(S, K, T, r, sigma, q = 0, op_type = 'call'):
    d1 = (np.log(S/K) + T * (r + (sigma**2)/2))/(sigma * np.sqrt(T))
    d2 = d1 - (sigma * np.sqrt(T))
    if op_type == 'call':
        call_value = S * np.exp(-q * T) * norm.cdf(d1, 0, 1) - K * np.exp(-r * T) * norm.cdf(d2, 0, 1)
        return call_value
    else:
        put_value = K * np.exp(-r * T) * norm.cdf(-d2, 0 , 1) - S * np.exp(-q * T) * norm.cdf(-d1, 0, 1)
        return put_value

S = 100.0   # price of the underlying
K = 110.0   # strike price
T = 0.8     # time to maturity in years
r = 0.05    # annualised risk-free rate
sigma = 0.2 # realised volatility 
q = 0.0     # the dividend yield   

ref_call = bsm_ref.BlackScholesCall(S, K, T, r, sigma, q)
ref_call_price = ref_call.price()

ref_put = bsm_ref.BlackScholesPut(S, K, T, r, sigma, q)
ref_put_price = ref_put.price()

def our_call(S, K, T, r, sigma, q):
    return bsm(S, K, T, r, sigma, q, op_type= 'call')

def our_put(S, K, T, r, sigma, q):
    return bsm(S, K, T, r, sigma, q, op_type= 'put')