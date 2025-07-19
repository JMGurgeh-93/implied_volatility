"""A simple attempt to model the Black-Scholes equation for calculating options
prices in python"""

import math 
import numpy as np
from scipy.stats import norm
import blackscholes as bsm_ref # reference function to check our model

# writing out the main BSM function

def bsm(S, K, T, r, sigma, q = 0, op_type = 'call'):
    d1 = (math.log(S/K) + T * (r + (sigma**2)/2))/(sigma * math.sqrt(T))
    d2 = d1 - (sigma * math.sqrt(T))
    if op_type == 'call':
        call_value = S * math.exp(-q * T) * norm.cdf(d1, 0, 1) - K * math.exp(-r * T) * norm.cdf(d2, 0, 1)
        return call_value
    else:
        put_value = K * math.exp(-r * T) * norm.cdf(-d2, 0 , 1) - S * math.exp(-q * T) * norm.cdf(-d1, 0, 1)
        return put_value

S = 100.0
K = 110.0
T = 0.8
r = 0.05
sigma = 0.2
q = 0.0

ref_call = bsm_ref.BlackScholesCall(S, K, T, r, sigma, q)
ref_call_price = ref_call.price()

ref_put = bsm_ref.BlackScholesPut(S, K, T, r, sigma, q)
ref_put_price = ref_put.price()

our_call = bsm(S, K, T, r, sigma, q, op_type= 'call')
our_put = bsm(S, K, T, r, sigma, q, op_type= 'put')

print("Our Call, Reference Call")
print(our_call, ref_call_price)
print("Our Put, Reference Put")
print(our_put, ref_put_price)