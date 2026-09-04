import math
import numpy as np
from scipy.stats import norm

# calculates a call option's price using black scholes equation
def calculateCallPrice(S, K, r, t, sigma):

    d1 = ( math.log(S/K) + (r + sigma**2 / 2) * t ) / ( sigma * math.sqrt(t) )
    d2 = d1 - sigma * math.sqrt(t)

    C = S * norm.cdf(d1) - K * math.exp(-r*t) * norm.cdf(d2)

    return C

# calculates a put option's price using black scholes equation
def calculatePutPrice(S, K, r, t, sigma):

    d1 = ( math.log(S/K) + (r + sigma**2 / 2) * t ) / ( sigma * math.sqrt(t) )
    d2 = d1 - sigma * math.sqrt(t)

    C = K * math.exp(-r*t) * norm.cdf(-d2) - S * norm.cdf(-d1)

    return C
