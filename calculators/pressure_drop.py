import streamlit as st
import math

from utils.layout import (
    page_header,
    engineering_notes, 
    footer
)

def calculate_friction_factor(
        reynolds, 
        roughness, 
        diameter
):
    """
    Calculate Darcy friction factor based on flow regime.
    """
    if reynolds <= 0: 
        raise ValueError("Reynolds number must be positive")

    if reynolds < 2300: 
        friction_factor = 64 / reynolds

    else: 
        friction_factor = (
            0.25 
            / (
                math.log10(
                    roughness / (3.7 * diameter)
                    + 5.74 / (reynolds ** 0.9)
                )
                ** 2
            )
        )
    return friction_factor

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
        * (density * velocity**2 / 2)
    )

    return pressure_drop

def validate_inputs(
        pipe_length, diameter,density,velocity,viscocity,roughness):
    """
    Validate physical inputs for the pressure drop calculation.
    """
    if pipe_length <= 0: 
        return "Pipe length must be greater than zero."
    if diameter <= 0: 
        return "Diameter must be greater than zero."
    if density <= 0: 
        return "Density must be greater than zero."
    if velocity < 0: 
        return "Velocity cannot be negative."
    if roughness < 0: 
        return "Pipe roughness cannot be negative."

    return None

def show(): 
    page_header(
        "📉 Pipe Pressure Drop",
        """
        Calculate pressure loss caused by
        friction in a pipe.
        """
    )

    viscosity = st.number_input(
        "Dynamic Viscosity (Pa·s)", 
        value = 0.001, 
        min_value=0.000001, 
        format="%.6f"
    )

    roughness = st.number_input(
        "Pipe Roughness (m)", 
        value = 0.000045, 
        min_value=0.0,
        format = "%.8f"
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

        error = validate_inputs(
            pipe_length, diameter, density, velocity, viscosity, roughness
        )
        if error: 
            st.error(error)
            return 

        reynolds = (density * velocity * diameter / viscosity)

        if reynolds < 2300: 
            flow_regime = "Laminar"
        elif reynolds <= 4000: 
            flow_regime = "Transitional" 
        else: 
            flow_regime = "Turbulent"

        if flow_regime == "Transitional":
            st.warning(
                "Flow is transitional." 
                "The friction factor estimate may be less reliable in this regime"
            )

        friction_factor = calculate_friction_factor(
            reynolds, roughness, diameter
        ) 

        pressure_drop = calculate_pressure_drop(friction_factor, pipe_length, diameter, density, velocity)

        st.success("Calculation Complete")

        st.metric("Reynolds Number", f"{reynolds:.0f}")

        st.metric("Flow Regime", flow_regime)

        st.metric("Friction Factor", f"{friction_factor:.5f}")

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