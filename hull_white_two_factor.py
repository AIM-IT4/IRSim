import numpy as np


def simulate_hw2(kappa1, kappa2, theta1, theta2, sigma1, sigma2, r0, s0, n_steps, dt, n_simulations):
    r = np.zeros((n_simulations, n_steps))
    s = np.zeros((n_simulations, n_steps))
    r[:, 0] = r0
    s[:, 0] = s0
    for t in range(1, n_steps):
        dW1 = np.sqrt(dt) * np.random.normal(0, 1, n_simulations)
        dW2 = np.sqrt(dt) * np.random.normal(0, 1, n_simulations)
        dr = kappa1 * (theta1 - r[:, t-1]) * dt + sigma1 * dW1
        ds = kappa2 * (theta2 - s[:, t-1]) * dt + sigma2 * dW2
        r[:, t] = r[:, t-1] + dr
        s[:, t] = s[:, t-1] + ds
    return r, s



import matplotlib.pyplot as plt

def plot_hullwhitetwofactor(results, n_paths=10):
    plt.figure(figsize=(10, 6))
    for i in range(min(n_paths, results.shape[0])):
        plt.plot(results[i, :], label=f'Simulation {i+1}')
    plt.title('Hull White Two Factor - Monte Carlo Simulations')
    plt.xlabel('Time')
    plt.ylabel('Interest Rate')
    plt.legend()
    plt.grid(True)
    plt.show()
