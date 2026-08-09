import streamlit as st

from utils.layout import (
    page_header,
    engineering_notes, 
    footer
)

def calculate_pressure_drop(
        friction_factor, 
        pipe_length, 
        diameter, 
        density, 
        velocity
): 
    """
    Calculate pressure drop using the Darcy-Weisbach equation.
    """
    pressure_drop = (
        friction_factor
        * (pipe_length / diameter) 
        * (density * velocity ** 2 / 2)
    )

    return pressure_drop

def show(): 
    page_header(
        "📉 Pipe Pressure Drop",
        """
        Calculate pressure loss caused by
        friction in a pipe.
        """
    )

    friction_factor = st.number_input(
        "Darcy Friction Factor", 
        value = 0.02, 
        min_value=0.0001
    )

    pipe_length = st.number_input(
        "Pipe Length (m)", 
        value=10.0, 
        min_value=0.0001
    )

    diameter = st.number_input(
        "Pipe Diameter (m)", 
        value=0.10, 
        min_value=0.0001
    )

    density = st.number_input(
        "Fluid Density (kg/m³)", 
        value=1000.0, 
        min_value=0.0001
    )

    velocity = st.number_input(
        "Veloctiy (m/s)", 
        value=1.0, 
        min_value=0.0
    )

    if st.button("Calculate Pressure Drop"): 
        pressure_drop = calculate_pressure_drop(friction_factor, pipe_length, diameter, density, velocity)

        st.success("Calculation Complete")

        st.metric("Pressure Drop", f"{pressure_drop:.2f} Pa")

    engineering_notes(
        """
        Darcy-Weisbach equation:

        ΔP = f(L/D)(ρv²/2)

        The friction factor depends on
        factors such as Reynolds Number
        and pipe roughness.
        """
    )

    footer()