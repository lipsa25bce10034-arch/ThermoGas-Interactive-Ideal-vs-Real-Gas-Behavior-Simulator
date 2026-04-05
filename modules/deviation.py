import numpy as np

"""
This file calculates deviation between ideal and real gas behavior
"""


def calculate_deviation(ideal_values, real_values):
    """
    Calculate percentage deviation

    Formula:
    % deviation = |real - ideal| / ideal * 100
    """

    deviation = np.abs((real_values - ideal_values) / ideal_values) * 100
    avg_deviation = np.mean(deviation)

    return deviation, avg_deviation


def max_deviation(deviation):
    """
    Returns maximum deviation value
    """
    return np.max(deviation)
