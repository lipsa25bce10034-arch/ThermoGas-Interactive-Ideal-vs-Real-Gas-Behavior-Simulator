import numpy as np

"""
This file contains functions related to basic gas laws:
Boyle's Law, Charles Law, and Gay-Lussac Law
"""

# Boyle's Law: P ∝ 1/V (at constant temperature)
def boyles_law(volume, k):
    """
    Calculate pressure using Boyle's Law

    Parameters:
    volume (array): Volume values
    k (float): Constant (P * V)

    Returns:
    array: Pressure values
    """
    return k / volume


# Charles Law: V ∝ T (at constant pressure)
def charles_law(temperature, k):
    """
    Calculate volume using Charles Law

    Parameters:
    temperature (array): Temperature values (K)
    k (float): Constant

    Returns:
    array: Volume values
    """
    return k * temperature


# Gay-Lussac Law: P ∝ T (at constant volume)
def gay_lussac_law(temperature, k):
    """
    Calculate pressure using Gay-Lussac Law

    Parameters:
    temperature (array): Temperature values (K)
    k (float): Constant

    Returns:
    array: Pressure values
    """
    return k * temperature
