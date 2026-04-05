import matplotlib.pyplot as plt

"""
This file contains graphs comparing Ideal vs Real gas behavior
and deviation visualization.
"""


def plot_ideal_vs_real(volume, ideal_pressure, real_pressure):
    """
    Plot comparison graph between Ideal Gas and Real Gas
    """
    fig, ax = plt.subplots()

    ax.plot(volume, ideal_pressure, linestyle='--', label="Ideal Gas", color='blue')
    ax.plot(volume, real_pressure, label="Real Gas", color='orange')

    ax.set_xlabel("Volume (V)")
    ax.set_ylabel("Pressure (P)")
    ax.set_title("Ideal vs Real Gas Behavior")
    ax.legend()
    ax.grid(True)

    return fig


def plot_deviation(volume, deviation):
    """
    Plot deviation (%) vs volume
    """
    fig, ax = plt.subplots()

    ax.plot(volume, deviation, color='purple')

    ax.set_xlabel("Volume (V)")
    ax.set_ylabel("Deviation (%)")
    ax.set_title("Percentage Deviation of Real Gas from Ideal Gas")
    ax.grid(True)

    return fig
