import numpy as np
import matplotlib.pyplot as plt
from blackScholes import calculateCallPrice
from MonteCarloSimulator import estimateOptionPrice
from relationshipMeasurer import calculateRelationship

# Black-Scholes parameters
S = 100
K = 100
r = 0.05
t = 1
sigma = 0.2

blackScholesPrice = calculateCallPrice(S, K, r, t, sigma)

# Number of Monte Carlo paths
simulationSizes = np.concatenate((
    np.arange(5000, 100000, 5000),
    np.arange(100000, 1000001, 10000)
))

# Repeat each experiment several times
repetitions = 20

meanErrors = []

for n in simulationSizes:

    repeatedErrors = []

    for _ in range(repetitions):
        simulatedPrice = estimateOptionPrice(
            S, K, r, t, sigma, "call", n
        )

        error = abs(blackScholesPrice - simulatedPrice)
        repeatedErrors.append(error)

    meanErrors.append(np.mean(repeatedErrors))

meanErrors = np.array(meanErrors)

# Fit power law:
# E(N) = a * N^b
a, b, correlation = calculateRelationship(
    simulationSizes,
    meanErrors
)

fittedErrors = a * simulationSizes**b


# Plot

plt.scatter(
    simulationSizes,
    meanErrors,
    label="Mean Monte Carlo Error"
)

plt.plot(
    simulationSizes,
    fittedErrors,
    label=fr"Fit: $E(N)={a:.3f}N^{{{b:.3f}}}$, $r={correlation:.4f}$"
)

plt.xscale("log")
plt.yscale("log")

plt.xlabel("Number of simulations")
plt.ylabel("Mean(20 iterations) absolute pricing error")

plt.title(
    "Monte Carlo Convergence to the Black-Scholes Price"
)

plt.legend()

plt.show()