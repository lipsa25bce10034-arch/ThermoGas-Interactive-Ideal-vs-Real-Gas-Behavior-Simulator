import matplotlib.pyplot as plt

"""
This file contains functions to generate graphs
for basic gas laws.
"""


def plot_boyles_law(volume, pressure):
    """
    Plot Pressure vs Volume graph (Boyle's Law)
    """
    fig, ax = plt.subplots()
    ax.plot(volume, pressure, color='blue')
    ax.set_xlabel("Volume (V)")
    ax.set_ylabel("Pressure (P)")
    ax.set_title("Boyle's Law (P vs V)")
    ax.grid(True)
    return fig


def plot_charles_law(temperature, volume):
    """
    Plot Volume vs Temperature graph (Charles Law)
    """
    fig, ax = plt.subplots()
    ax.plot(temperature, volume, color='green')
    ax.set_xlabel("Temperature (K)")
    ax.set_ylabel("Volume (V)")
    ax.set_title("Charles Law (V vs T)")
    ax.grid(True)
    return fig


def plot_gay_lussac_law(temperature, pressure):
    """
    Plot Pressure vs Temperature graph (Gay-Lussac Law)
    """
    fig, ax = plt.subplots()
    ax.plot(temperature, pressure, color='red')
    ax.set_xlabel("Temperature (K)")
    ax.set_ylabel("Pressure (P)")
    ax.set_title("Gay-Lussac Law (P vs T)")
    ax.grid(True)
    return fig
