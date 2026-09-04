import numpy as np

def estimateOptionPrice(S, K, r, t, sigma, type="call", nSims=10000):

    rng = np.random.default_rng()
    Z = rng.standard_normal(nSims)

    St = S * np.exp(
        (r - 0.5 * sigma**2) * t + 
        sigma * np.sqrt(t) * Z
    )

    if (type == "call"):
        payoff = np.maximum(St - K, 0)
    else:
        payoff = np.maximum(K - St, 0)

    estimatedPrice = np.mean(payoff * np.exp(-r*t))

    return estimatedPrice
