import numpy as np


def simulate_lmm(sigma_lmm, L0, n_steps, dt, n_simulations):
    L = np.zeros((n_simulations, n_steps))
    L[:, 0] = L0
    for t in range(1, n_steps):
        dW = np.sqrt(dt) * np.random.normal(0, 1, n_simulations)
        dL = sigma_lmm * L[:, t-1] * dW
        L[:, t] = L[:, t-1] + dL
    return L



import matplotlib.pyplot as plt

def plot_lmm(results, n_paths=10):
    plt.figure(figsize=(10, 6))
    for i in range(min(n_paths, results.shape[0])):
        plt.plot(results[i, :], label=f'Simulation {i+1}')
    plt.title('Lmm - Monte Carlo Simulations')
    plt.xlabel('Time')
    plt.ylabel('Interest Rate')
    plt.legend()
    plt.grid(True)
    plt.show()
