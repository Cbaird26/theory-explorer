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
    st.header("Educational Modules")
    st.write("Learn about the Theory of Everything.")

    modules = {
        "General Relativity": "General Relativity describes the gravitational force as the curvature of spacetime caused by mass and energy.",
        "Quantum Mechanics": "Quantum Mechanics deals with the behavior of particles at atomic and subatomic scales.",
        "String Theory": "String Theory posits that particles are one-dimensional strings vibrating at different frequencies.",
        "Loop Quantum Gravity": "Loop Quantum Gravity attempts to describe the quantum properties of the universe and gravity."
    }

    module = st.selectbox("Select a Module", list(modules.keys()))
    st.write(modules[module])

# Build Your Own Universe
if page == "Build Your Own Universe":
    st.header("Build Your Own Universe")
    st.write("Manipulate initial conditions and see how the universe evolves.")

    initial_density = st.sidebar.slider("Initial Density", 0.1, 10.0, 1.0)
    initial_temperature = st.sidebar.slider("Initial Temperature (K)", 1, 10000, 3000)

    st.write(f"Simulating universe with initial density {initial_density} and temperature {initial_temperature} K.")

    # Simple universe evolution simulation
    def universe_evolution(density, temperature, t):
        # Simplified model for demonstration
        size = density * np.exp(-0.1 * t) + temperature * np.exp(0.1 * t)
        return size

    time_points = np.linspace(0, 100, 200)
    universe_size = universe_evolution(initial_density, initial_temperature, time_points)

    fig, ax = plt.subplots()
    ax.plot(time_points, universe_size)
    ax.set_xlabel("Time")
    ax.set_ylabel("Universe Size")
    st.pyplot(fig)

# Particle Collider
if page == "Particle Collider":
    st.header("Particle Collider")
    st.write("Run virtual particle collisions and observe the outcomes.")

    collision_energy = st.sidebar.slider("Collision Energy (TeV)", 1, 100, 13)
    particles = ["Electron", "Proton", "Neutron", "Higgs Boson"]
    particle = st.sidebar.selectbox("Select a Particle", particles)

    st.write(f"Running collisions at {collision_energy} TeV involving {particle}.")

    # Placeholder for detailed particle collision outcomes
    st.write("Collision outcomes will be displayed here.")

    # Example of a simple collision result display
    st.write(f"Simulated collision of {particle} at {collision_energy} TeV results in:")
    if particle == "Electron":
        st.write("Result: High energy electrons and photons.")
    elif particle == "Proton":
        st.write("Result: Quarks and gluons, forming jets.")
    elif particle == "Neutron":
        st.write("Result: Quarks and gluons, forming hadronic showers.")
    elif particle == "Higgs Boson":
        st.write("Result: Decays into various particles, including bottom quarks, W bosons, and photons.")
