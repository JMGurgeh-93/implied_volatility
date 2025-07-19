# calculating the 'Greeks' 

import bsm_model
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
ds = 1e-5

def delta_fdm_call(S, K, T, r, sigma, q, ds):
    return (bsm_model.our_call(S + ds, K, T, r, sigma, q) - bsm_model.our_call(S, K, T, r, sigma, q))/ds

def delta_fdm_put(S, K, T, r, sigma, q, ds):
    return (bsm_model.our_put(S + ds, K, T, r, sigma, q) - bsm_model.our_put(S, K, T, r, sigma, q))/ds

# using arange to generate a set of prices against which we can plot the delta
prices = np.arange(1, 300, 1)
deltas_call = delta_fdm_call(prices, K, T, r, sigma, q)
deltas_put = delta_fdm_put(prices, K, T, r, sigma, q)

