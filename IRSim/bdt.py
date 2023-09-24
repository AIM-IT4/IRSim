import numpy as np


def simulate_bdt(sigma_bdt, r0_bdt, n_periods):
    tree = np.zeros((n_periods, n_periods))
    tree[0, 0] = r0_bdt
    for t in range(1, n_periods):
        tree[t, 0] = tree[t-1, 0] * np.exp(-sigma_bdt * np.sqrt(dt))
        for j in range(1, t+1):
            tree[t, j] = tree[t-1, j-1] * np.exp(sigma_bdt * np.sqrt(dt))
    return tree



import matplotlib.pyplot as plt

def plot_bdt(results, n_paths=10):
    plt.figure(figsize=(10, 6))
    for i in range(min(n_paths, results.shape[0])):
        plt.plot(results[i, :], label=f'Simulation {i+1}')
    plt.title('Bdt - Monte Carlo Simulations')
    plt.xlabel('Time')
    plt.ylabel('Interest Rate')
    plt.legend()
    plt.grid(True)
    plt.show()
