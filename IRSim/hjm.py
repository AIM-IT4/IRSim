import numpy as np


def simulate_hjm(sigma_hjm, f0, n_steps, dt, n_simulations):
    f = np.zeros((n_simulations, n_steps))
    f[:, 0] = f0
    for t in range(1, n_steps):
        dW = np.sqrt(dt) * np.random.normal(0, 1, n_simulations)
        df = sigma_hjm * dW
        f[:, t] = f[:, t-1] + df
    return f



import matplotlib.pyplot as plt

def plot_hjm(results, n_paths=10):
    plt.figure(figsize=(10, 6))
    for i in range(min(n_paths, results.shape[0])):
        plt.plot(results[i, :], label=f'Simulation {i+1}')
    plt.title('Hjm - Monte Carlo Simulations')
    plt.xlabel('Time')
    plt.ylabel('Interest Rate')
    plt.legend()
    plt.grid(True)
    plt.show()
