import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import plotly.graph_objects as go

# Title and description
st.title("Theory Explorer")
st.write("""
    Welcome to the Theory Explorer! This app lets you explore the fascinating world of the Theory of Everything through interactive simulations and visualizations.
""")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Black Hole Dynamics", "Cosmic Evolution", "Particle Physics", "Educational Modules", "Build Your Own Universe", "Particle Collider"])

# Home page
if page == "Home":
    st.header("Home")
    st.write("""
        Explore the various aspects of the Theory of Everything through this interactive application. Use the navigation panel to explore different sections.
    """)

# Black Hole Dynamics
if page == "Black Hole Dynamics":
    st.header("Black Hole Dynamics")
    st.write("Simulating the dynamics of a black hole.")

    mass = st.sidebar.slider("Black Hole Mass", 1, 100, 10)
    time = st.sidebar.slider("Simulation Time", 1, 100, 10)

    def black_hole_growth(m, t):
        return 0.1 * m

    time_points = np.linspace(0, time, 100)
    mass_points = odeint(black_hole_growth, mass, time_points)

    fig, ax = plt.subplots()
    ax.plot(time_points, mass_points)
    ax.set_xlabel("Time")
    ax.set_ylabel("Black Hole Mass")
    st.pyplot(fig)

# Cosmic Evolution
if page == "Cosmic Evolution":
    st.header("Cosmic Evolution")
    st.write("Visualize the evolution of the universe.")

    inflation_time = np.linspace(0, 1, 100)
    inflation_size = np.exp(inflation_time)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=inflation_time, y=inflation_size, mode='lines', name='Cosmic Inflation'))
    fig.update_layout(title='Cosmic Evolution', xaxis_title='Time', yaxis_title='Universe Size')
    st.plotly_chart(fig)

# Particle Physics
if page == "Particle Physics":
    st.header("Particle Physics")
    st.write("Explore particle interactions.")

    collision_energy = st.sidebar.slider("Collision Energy (TeV)", 1, 100, 13)
    particles = ["Electron", "Proton", "Neutron", "Higgs Boson"]
    particle = st.sidebar.selectbox("Select a Particle", particles)

    st.write(f"Simulating collisions at {collision_energy} TeV involving {particle}.")

    # Placeholder for particle collision simulation
    def simulate_particle_collision(energy, particle):
        # Simulate some basic results
        result = {
            "Electron": {"mass": 0.511, "charge": -1},
            "Proton": {"mass": 938.3, "charge": +1},
            "Neutron": {"mass": 939.6, "charge": 0},
            "Higgs Boson": {"mass": 125100, "charge": 0}
        }
        return result.get(particle, {})

    collision_result = simulate_particle_collision(collision_energy, particle)
    st.write(f"Collision result: {collision_result}")

# Educational Modules
if page == "Educational Modules":
    st.header("Ed
