import pandas as pd

"""
This file contains helper functions used across the project
"""

# -------------------------------
# Load Gas Constants from CSV
# -------------------------------
def load_gas_data(file_path="data/gas_constants.csv"):
    """
    Load gas constants dataset

    Returns:
    DataFrame containing gas data
    """
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        return None


# -------------------------------
# Get 'a' and 'b' values for gas
# -------------------------------
def get_gas_constants(df, gas_name):
    """
    Fetch a and b constants for selected gas

    Parameters:
    df : DataFrame
    gas_name : string

    Returns:
    (a, b)
    """
    gas_row = df[df["Gas"] == gas_name]

    if not gas_row.empty:
        a = gas_row["a"].values[0]
        b = gas_row["b"].values[0]
        return a, b
    else:
        return None, None


# -------------------------------
# Format Output Values
# -------------------------------
def format_value(value, precision=3):
    """
    Format numerical output for display
    """
    return f"{value:.{precision}f}"


# -------------------------------
# Validate Inputs
# -------------------------------
def validate_positive(value, name="Value"):
    """
    Ensure input values are positive
    """
    if value <= 0:
        raise ValueError(f"{name} must be greater than zero")
    return value
