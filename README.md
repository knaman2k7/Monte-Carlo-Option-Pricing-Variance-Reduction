# Monte Carlo Option Pricing: Convergence and Variance Reduction

In this project, I will be investigating European Option Pricing using Monte Carlo Simulation, benchmarked against the analytical Black-Scholes solution.
The main points of investigation are the convergence rate of Monte Carlo pricing and the effectiveness of antithetic variates as a variance-reduction technique.

## 1 Overview

The Black-Scholes model provides a closed-form solution for European Option pricing under a set of assumptions. Monte Carlo methods provide an alternative approach to this using a numerical approach. Possible stock prices are simulated and the discounted average payoff is used as an estimate.
This project uses the black-scholes price as a benchmark to investigate relations between pricing accuracy with number of simulations. I then implement antithetic variates to investigate whether the estimate's variance can be reduced in the same simulation budget.


## 2 Mathematical Background

### 2.1 Black-Scholes Price

For a European call option, the Black-Scholes price is:

```math
C = S_0N(d_1) - Ke^{-rT}N(d_2)
```

where:

```math
d_1 = \frac{\ln(S_0/K) + (r + \frac{1}{2}\sigma^2)T}{\sigma\sqrt{T}}
```

```math
d_2 = d_1 - \sigma\sqrt{T}
```

This is used as the benchmark for the Monte Carlo estimates.

### 2.2 Monte Carlo Simulation

The stock price at expiry is simulated using:

```math
S_T = S_0\exp\left(\left(r-\frac{1}{2}\sigma^2\right)T+\sigma\sqrt{T}Z\right)
```

where:

```math
Z \sim N(0,1)
```

For a European call option, the payoff is:

```math
\max(S_T-K,0)
```

Using \(N\) simulations, the Monte Carlo estimate is:

```math
\hat{C}_N = e^{-rT}\frac{1}{N}\sum_{i=1}^{N}\max(S_T^{(i)}-K,0)
```

### 2.3 Convergence

Monte Carlo error decreases approximately at the rate:

```math
O(N^{-1/2})
```

The absolute pricing error is:

```math
|\hat{C}_N - C_{BS}|
```

### 2.4 Antithetic Variates

Antithetic variates use pairs of random values:

```math
Z \quad \text{and} \quad -Z
```

These produce negatively related simulated outcomes, helping to reduce the variance of the Monte Carlo estimator.


## 3 Implementation

Here are the parameters I used throughout the project:

S₀ = 100
K  = 100
r  = 0.05
T  = 1
σ  = 0.20

The simulation was implemented in Python using NumPy for vectorised random sampling and numerical operations. SciPy's normal CDF was used in the Black–Scholes implementation, while Matplotlib was used for visualisation.

### 3.1 - Distrubution of simulated stock prices

![postively skewed price distrubution](plots/StockPriceDistrubution.png)

The simulated terminal stock prices form a positively skewed distrubution, as expected from the lognormal distrubution implied by Geometric Brownian Motion. Unlike a normal distribution, simulated prices cannot become negative and there is a longer upper tail.


### 3.2 - Convergence to Black-Scholes

![postively skewed price distrubution](plots/priceConvergence.png)

As the graph implies, at very small simulation sizes, the Monte Carlo estimate varies substantially from the Black-Scholes benchmark. As the number of simulations increases, the estimate stabilises increasingly close to the analytical price.
The logarthmic x-axis make the large range of simulation sizes visible on a single plot.


