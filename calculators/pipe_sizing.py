import streamlit as st
from calculators.pressure_drop import (calculate_pressure_drop, calculate_friction_factor)

def find_pipe_diameter(
        pipe_length, density, velocity, viscosity, roughness, max_pressure_drop
):
    """
    Find the smallest pipe diameter that satisfies the maximum allowable pressure drop.
    """
    diameters = [
        0.01 + i * 0.001
        for i in range(200)
    ]

    for diameter in diameters:
        reynolds = (density * velocity * diameter /viscosity)
        friction_factor = calculate_friction_factor(
            reynolds, roughness, diameter
        )
        pressure_drop = calculate_pressure_drop(
            friction_factor, pipe_length, diameter, density, velocity
        )
        if pressure_drop <= max_pressure_drop:
            return diameter, pressure_drop

    return None, None

def show():
    st.title("🔧 Pipe Sizing Calculator")
    st.write(
        """
        Estimate the minimum pipe diameter required to keep pressure drop below a specified limit.
        """
    )
    pipe_length = st.number_input(
        "Pipe Length (m)", 
        value=20.0, 
        min_value=0.1
    )
    density = st.number_input(
        "Fluid Density (kg/m³)", 
        value=1000.0,
        min_value=0.1
    )
    velocity = st.number_input(
        "Fluid Velocity (m/s)", 
        value=2.0, 
        min_value=0.01
    )
    viscosity = st.number_input(
        "Dynamic Viscosity (Pa·s)",
        value=0.001, 
        min_value=0.000001,
        format="%.6f"
    )
    roughness = st.number_input(
        "Aboslute Roughness (m)",
        value=0.0000045,
        min_value=0.0,
        format="%.6f"
    )
    max_pressure_drop = st.number_input(
        "Maximum Pressure Drop (Pa)",
        value=50000.0,
        min_value=1.0
    )

    if st.button("Find Pipe Diameter"):
        diameter, pressure_drop = find_pipe_diameter(
            pipe_length, density, velocity, viscosity, roughness, max_pressure_drop
        )
        if diameter is None:
            st.error(
                "No suitable pipe diameter was found"
                "within the search range."
            )
        else: 
            st.success(
                f"Required Pipe Diameter:"
                f"{diameter:.3f} m"
            )
            st.metric(
                "Estimated Pressure Drop", f"{pressure_drop:2f} Pa"
            )
            st.info(
                """
                The calculator searches through candidate pipe diameters and selects 
                the smallest diameter whose estimated pressure drop 
                satisfies the specified design constraint.
                """
            )