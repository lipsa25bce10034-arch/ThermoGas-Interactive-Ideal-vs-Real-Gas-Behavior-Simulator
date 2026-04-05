"""
This file contains Real Gas calculations using Van der Waals Equation
"""

R = 0.0821


def van_der_waals_pressure(n, T, V, a, b):
    """
    Calculate pressure for real gas using Van der Waals equation

    (P + a/V^2)(V - b) = nRT

    Parameters:
    n : moles
    T : temperature (K)
    V : volume (L)
    a : attraction constant
    b : volume correction constant

    Returns:
    Pressure (atm)
    """
    return ((n * R * T) / (V - n * b)) - (a * (n ** 2) / (V ** 2))


def van_der_waals_volume(n, T, P, a, b):
    """
    Approximate volume calculation (simplified version)

    Note: Exact solution requires solving cubic equation
    """
    return (n * R * T / P) + b
