import numpy as np
import matplotlib.pyplot as plt
from blackScholes import calculateBSOptionPrice
from MonteCarloSimulator import monteCarloOptionPrice, monteCarloStockPrice
from relationshipMeasurer import calculateRelationship

# Underlying Stock's parameters
S = 100
K = 100
r = 0.05
t = 1
sigma = 0.2


# Monte Carlo stock pricing distrbution
def graphPricingDistrbution():

    simulatedPrices = monteCarloStockPrice(S,r,t,sigma,nSims=100000)

    plt.hist(simulatedPrices, bins=200)

    plt.xlabel("Stock Price at Maturity")
    plt.ylabel("Frequency")
    plt.title("Distribution of Simulated Stock Prices at Maturity")

    plt.show()


# Monte Carlo convergence with Black Scholes price
def graphPricingConvergence():

    bsPrice = calculateBSOptionPrice(S,K,r,t,sigma)

    simulationSizes = [
        10,
        100,
        1000,
        10000,
        100000,
        1000000,
        10000000,
        100000000
    ]

    simulatedOptionPrices = []

    for n in simulationSizes:
        simulatedOptionPrices.append( 
            monteCarloOptionPrice(S,K,r,t,sigma,nSims=n)
        )

    plt.plot(
        simulationSizes,
        simulatedOptionPrices,
        marker="o",
        label="Simulated Option Price"
    )

    plt.axhline(
        bsPrice,
        label="Black Scholes Price"
    )

    plt.xscale("log")

    plt.xlabel("Number of Monte Carlo Simulations")
    plt.ylabel("Estimated Option Price")
    plt.title("Monte Carlo Option Price Convergence to Black-Scholes")

    plt.legend()
    plt.show()




# Calculate mean pricing error for each simulation size
def calculateConvergenceErrors(variates="normal"):

    bsPrice = calculateBSOptionPrice(S,K,r,t,sigma)
    
    simulationSizes = np.concatenate((
        np.arange(5000, 100000, 5000),
        np.arange(100000, 1000001, 10000)
    ))

    # by corresponding simulation sizes
    averageErrors = []

    iterations = 20
    for n in simulationSizes:

        errors = []

        for _ in range(iterations):

            simulatedPrice = monteCarloOptionPrice(S,K,r,t,sigma, nSims=n, variates=variates)
            errors.append( np.abs(simulatedPrice - bsPrice) )

        averageErrors.append( np.mean(errors) )

    a,b, correlation = calculateRelationship(simulationSizes,averageErrors)

    return [simulationSizes, averageErrors, a,b, correlation] if variates=="normal" else [averageErrors, a,b, correlation]




# Error vs Simulations
def graphErrorNrelation():

    simulationSizes, averageErrors, a,b, correlation = calculateConvergenceErrors()

    # plot

    a,b, correlation = calculateRelationship(simulationSizes,averageErrors)

    plt.scatter(
        simulationSizes,
        averageErrors,
        label="Mean Monte Carlo Error"
    )

    plt.plot(
        simulationSizes,
        a * simulationSizes**b,
        label=fr"Fit: $E(N)={a:.3f}N^{{{b:.3f}}}$, $r={correlation:.4f}$"
    )


    plt.xscale("log")
    plt.yscale("log")

    plt.xlabel("Number of Simulations")
    plt.ylabel("Mean Absolute Pricing Error (20 iterations)")
    plt.title("Monte Carlo Pricing Error vs. Number of Simulations")

    plt.legend()
    plt.show()


# 
def graphNormalAgainstAntithetical():

    simulationSizes, normalAverageErrors, normala, normalb, normalCorrelation = calculateConvergenceErrors()
    antitheticAverageErrors, antithetica, antitheticb, antitheticCorrelation = calculateConvergenceErrors("antithetic")

    # plot

    # normal
    plt.scatter(
        simulationSizes,
        normalAverageErrors,
        label="Standard Monte Carlo",
        color="blue"
    )
    plt.plot(
        simulationSizes,
        normala * simulationSizes**normalb,
        label=fr"Fit: $E(N)={normala:.3f}N^{{{normalb:.3f}}}$, $r={normalCorrelation:.4f}$",
        color="blue"
    )


    # antithetical
    plt.scatter(
        simulationSizes,
        antitheticAverageErrors,
        label="Antithetic Monte Carlo",
        color="red"
    )
    plt.plot(
        simulationSizes,
        antithetica * simulationSizes**antitheticb,
        label=fr"Fit: $E(N)={antithetica:.3f}N^{{{antitheticb:.3f}}}$, $r={antitheticCorrelation:.4f}$",
        color="red"
    )


    plt.xscale("log")
    plt.yscale("log")

    plt.xlabel("Number of Simulations")
    plt.ylabel("Mean Absolute Pricing Error (20 iterations)")
    plt.title("Standard vs. Antithetic Monte Carlo Pricing Error")

    plt.legend()
    plt.show()


graphNormalAgainstAntithetical()
