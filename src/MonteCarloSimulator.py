import numpy as np

def monteCarloStockPrice(S,r,t,sigma, Z=None, nSims=1000):

    if Z is None:
        rng = np.random.default_rng()
        Z = rng.standard_normal(nSims)

    St = S * np.exp(
        (r - 0.5 * sigma**2) * t + 
        sigma * np.sqrt(t) * Z
    )

    return St


def monteCarloOptionPrice(
    S, K, r, t, sigma, type="call", nSims=100,
    returnType="mean", variates="normal"
                        ):


    # Generate random values from standard normal distrubution
    rng = np.random.default_rng()
    if (variates == "antithetic"):
        Z = rng.standard_normal(nSims//2)
        Z = np.concatenate((Z, -Z))
    elif (variates == "normal"):
        Z = rng.standard_normal(nSims)
    else:
        raise ValueError("variates type should be 'normal' or 'antithetic'")


    # find stock price using the random values
    St = monteCarloStockPrice(S,r,t,sigma,Z=Z)


    # find the payoff of each stock price
    if (type == "call"):
        payoff = np.maximum(St - K, 0)
    else:
        payoff = np.maximum(K - St, 0)


    # return the discounted payoffs
    if (returnType == "mean"):
        return np.mean(payoff) * np.exp(-r*t)
    elif (returnType == "samples"):
        return payoff * np.exp(-r*t)
    else:
        raise ValueError("returnType must be 'mean' or 'samples'")
