#!/usr/bin/env python3
"""Example: plot a parametric curve and its tangent vector using matplotlib."""
import numpy as np
import matplotlib.pyplot as plt


def plot_curve(r_func, t_min=0, t_max=2 * np.pi, samples=400):
    t = np.linspace(t_min, t_max, samples)
    r = np.array([r_func(tt) for tt in t])
    x, y = r[:, 0], r[:, 1]
    dx = np.gradient(x, t)
    dy = np.gradient(y, t)

    plt.figure(figsize=(6, 6))
    plt.plot(x, y, label='curve')
    idx = samples // 4
    plt.quiver(x[idx], y[idx], dx[idx], dy[idx], scale=30, color='r', label='tangent')
    plt.axis('equal')
    plt.legend()
    plt.title('Parametric curve')
    plt.show()


if __name__ == '__main__':
    def r(t):
        return np.array([np.cos(2 * t) * (1 + 0.5 * np.cos(t)), np.sin(2 * t) * (1 + 0.5 * np.cos(t))])

    plot_curve(r)
