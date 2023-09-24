import numpy as np


def simulate_vasicek(a, b, sigma, r0, n_steps, dt, n_simulations):
    r = np.zeros((n_simulations, n_steps))
    r[:, 0] = r0
    for t in range(1, n_steps):
        dW = np.sqrt(dt) * np.random.normal(0, 1, n_simulations)
        dr = a * (b - r[:, t-1]) * dt + sigma * dW
        r[:, t] = r[:, t-1] + dr
    return r



import matplotlib.pyplot as plt

def plot_vasicek(results, n_paths=10):
    plt.figure(figsize=(10, 6))
    for i in range(min(n_paths, results.shape[0])):
        plt.plot(results[i, :], label=f'Simulation {i+1}')
    plt.title('Vasicek - Monte Carlo Simulations')
    plt.xlabel('Time')
    plt.ylabel('Interest Rate')
    plt.legend()
    plt.grid(True)
    plt.show()
