import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Constants
R = 0.0821  # L·atm/mol·K

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(page_title="ThermoGas Simulator", layout="wide")

st.title("🌡️ ThermoGas: Gas Behavior Simulator")

# Sidebar Menu
menu = st.sidebar.selectbox(
    "Select Module",
    ["Gas Law Graphs", "Ideal vs Real Gas", "Deviation Visualization"]
)

# -----------------------------
# 1. GAS LAW GRAPHS
# -----------------------------
if menu == "Gas Law Graphs":
    st.header("📊 Gas Law Graph Generator")

    law = st.selectbox(
        "Select Law",
        ["Boyle's Law (P-V)", "Charles Law (V-T)", "Gay-Lussac Law (P-T)"]
    )

    fig, ax = plt.subplots()

    if law == "Boyle's Law (P-V)":
        st.subheader("Boyle's Law: P ∝ 1/V")

        V = np.linspace(1, 10, 100)
        k = st.slider("Constant (k)", 1.0, 10.0, 5.0)
        P = k / V

        ax.plot(V, P)
        ax.set_xlabel("Volume")
        ax.set_ylabel("Pressure")
        ax.set_title("Pressure vs Volume")

    elif law == "Charles Law (V-T)":
        st.subheader("Charles Law: V ∝ T")

        T = np.linspace(100, 500, 100)
        k = st.slider("Constant (k)", 0.01, 0.1, 0.05)
        V = k * T

        ax.plot(T, V)
        ax.set_xlabel("Temperature")
        ax.set_ylabel("Volume")
        ax.set_title("Volume vs Temperature")

    else:
        st.subheader("Gay-Lussac Law: P ∝ T")

        T = np.linspace(100, 500, 100)
        k = st.slider("Constant (k)", 0.01, 0.1, 0.05)
        P = k * T

        ax.plot(T, P)
        ax.set_xlabel("Temperature")
        ax.set_ylabel("Pressure")
        ax.set_title("Pressure vs Temperature")

    st.pyplot(fig)

# -----------------------------
# 2. IDEAL VS REAL GAS
# -----------------------------
elif menu == "Ideal vs Real Gas":
    st.header("⚖️ Ideal vs Real Gas Simulator")

    # Inputs
    P = st.number_input("Pressure (atm)", value=1.0)
    V = st.number_input("Volume (L)", value=1.0)
    T = st.number_input("Temperature (K)", value=300.0)
    n = st.number_input("Moles (n)", value=1.0)

    st.subheader("Van der Waals Constants")
    a = st.number_input("a constant", value=1.36)
    b = st.number_input("b constant", value=0.031)

    # Ideal Gas
    ideal_P = (n * R * T) / V

    # Real Gas (Van der Waals)
    real_P = ((n * R * T) / (V - n * b)) - (a * (n**2) / (V**2))

    st.write(f"**Ideal Gas Pressure:** {ideal_P:.3f} atm")
    st.write(f"**Real Gas Pressure:** {real_P:.3f} atm")

# -----------------------------
# 3. DEVIATION VISUALIZATION
# -----------------------------
elif menu == "Deviation Visualization":
    st.header("📈 Deviation Visualization")

    V = np.linspace(0.5, 10, 100)
    T = 300
    n = 1

    a = st.slider("a constant", 0.1, 5.0, 1.36)
    b = st.slider("b constant", 0.01, 0.1, 0.03)

    # Ideal Gas
    ideal_P = (n * R * T) / V

    # Real Gas
    real_P = ((n * R * T) / (V - n * b)) - (a * (n**2) / (V**2))

    # Plot
    fig, ax = plt.subplots()
    ax.plot(V, ideal_P, label="Ideal Gas", linestyle="--")
    ax.plot(V, real_P, label="Real Gas")
    ax.set_xlabel("Volume")
    ax.set_ylabel("Pressure")
    ax.set_title("Ideal vs Real Gas Behavior")
    ax.legend()

    st.pyplot(fig)

    # Deviation Calculation
    
    deviation = np.abs((real_P - ideal_P) / ideal_P) * 100
    avg_dev = np.mean(deviation)

    st.write(f"**Average % Deviation:** {avg_dev:.2f}%")
