"""
Compressibility factor Z:
Z = PV / nRT

Used to check deviation from ideal behavior
Z = 1 → Ideal Gas
Z ≠ 1 → Real Gas
"""

R = 0.0821


def compressibility_factor(P, V, n, T):
    """
    Calculate compressibility factor Z

    Parameters:
    P : Pressure (atm)
    V : Volume (L)
    n : Moles
    T : Temperature (K)

    Returns:
    Z value
    """
    return (P * V) / (n * R * T)


def interpret_z(Z):
    """
    Interpret compressibility factor
    """
    if abs(Z - 1) < 0.05:
        return "Approximately Ideal Gas"
    elif Z > 1:
        return "Repulsive forces dominate"
    else:
        return "Attractive forces dominate"
