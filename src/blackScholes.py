import math
import numpy as np
from scipy.stats import norm

# calculates an option's price using black scholes equation
def calculateBSOptionPrice(S, K, r, t, sigma, type="call"):

    d1 = ( math.log(S/K) + (r + sigma**2 / 2) * t ) / ( sigma * math.sqrt(t) )
    d2 = d1 - sigma * math.sqrt(t)

    if (type=="call"):
        C = S * norm.cdf(d1) - K * math.exp(-r*t) * norm.cdf(d2)
    elif (type=="put"):
        C = K * math.exp(-r*t) * norm.cdf(-d2) - S * norm.cdf(-d1)
    else:
        raise ValueError("type should only be of type 'call' or 'put")

    return C

