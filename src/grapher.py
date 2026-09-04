import numpy as np
import matplotlib.pyplot as plt
from blackScholes import calculateCallPrice
from MonteCarloSimulator import estimateOptionPrice

S = 100
K = 100
r = 0.05
t = 1
sigma = 0.2

blackScholesPrice = calculateCallPrice(S, K, r, t, sigma)

simulationSizes = np.arange(20000, 1000001, 10000)
simulatedPrices = []

for n in simulationSizes:
    simulatedPrices.append( estimateOptionPrice(S,K,r,t,sigma,"call",n) )


#for n in simulationSizes:
#    price = estimateOptionPrice(S, K, r, t, sigma, "call", n)
#    simulatedPrices.append(price)

a = np.array(simulatedPrices)
b = np.abs(blackScholesPrice - a)


plt.plot(simulationSizes, b)

plt.xlabel("Number of simulations")
plt.ylabel("absolute error")
plt.ticklabel_format(axis="x", style="plain", useOffset=False)
plt.title("Monte Carlo Convergence to the Black-Scholes Price")

plt.show()