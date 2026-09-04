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

simulationSizes = np.array([
    10,
    100,
    1000,
    10000,
    100000,
    1000000,
    10000000,
    100000000,
    1000000000
])

simulatedPrices = []

for n in simulationSizes:
    price = estimateOptionPrice(S, K, r, t, sigma, "call", n)
    simulatedPrices.append(price)

a = np.array(simulatedPrices)
b = (a-blackScholesPrice) / blackScholesPrice

for i in range(len(b)):
    print(f"({simulationSizes[i]},{b[i]*100})")

plt.plot(
    simulationSizes,
    simulatedPrices,
    marker="o",
    label="Monte Carlo"
)
plt.axhline(blackScholesPrice, label="Black-Scholes")

plt.xscale("log")
plt.xlabel("Number of simulations")
plt.ylabel("Option price")
plt.legend()

plt.show()