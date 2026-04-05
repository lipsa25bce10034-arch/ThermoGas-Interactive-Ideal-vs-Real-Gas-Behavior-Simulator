"""
This file contains Ideal Gas Equation functions
PV = nRT
"""

R = 0.0821  # Gas constant (L·atm/mol·K)


def ideal_gas_pressure(n, T, V):
    """
    Calculate pressure using Ideal Gas Equation

    Parameters:
    n (float): Number of moles
    T (float or array): Temperature (K)
    V (float or array): Volume (L)

    Returns:
    float or array: Pressure (atm)
    """
    return (n * R * T) / V


def ideal_gas_volume(n, T, P):
    """
    Calculate volume from Ideal Gas Equation
    """
    return (n * R * T) / P


def ideal_gas_temperature(P, V, n):
    """
    Calculate temperature from Ideal Gas Equation
    """
    return (P * V) / (n * R)
