import streamlit as st 

from utils.layout import (
    page_header, 
    engineering_notes, 
    footer
)

def calculate_reynolds(
        density, 
        velocity, 
        diameter, 
        viscosity
):
    """
    Calculates the Reynolds Number
    """

    return (
        density *
        velocity * 
        diameter
    ) / viscosity

def classify_flow(reynolds): 
    """
    Classify the flow regime. 
    """

    if reynolds < 2300: 
        return "Laminar" 

    elif reynolds <= 4000: 
        return "Transitional" 

    else: 
        return "Turbulent"

def show(): 

    page_header(
        "🌊 Reynolds Number Calculator",
        """
        Calculate Reynolds Number and determine
        whether flow is laminar, transitional,
        or turbulent.
        """   
    )

    density = st.number_input(
        "Density (kg/m³)", 
        value = 1000.0, 
        min_value = 0.0001
    )

    velocity = st.number_input(
        "Velocity(m/s)", 
        value = 1.0, 
        min_value = 0.0 
    )

    diameter = st.number_input(
        "Pipe Diameter (m)", 
        value = 1.0, 
        min_value = 0.0
    )

    viscosity = st.number_input(
        "Dynamic Viscosity (Pa·s)", 
        value = 0.001, 
        min_value = 0.000001, 
        format = "%.6f"
    )

    if st.button("Calculate"): 

        reynolds = calculate_reynolds(
            density, 
            velocity, 
            diameter, 
            viscosity
        )

        regime = classify_flow(reynolds)

        st.success("Calculation Complete")

        st.metric(
            "Reynolds Number", 
            f"{reynolds:.0f}"
        )

        if regime == "Laminar": 
            st.info("Flow Regime: Laminar")

        elif regime == "Transitional": 
            st.warning("Flow Regime: Transitional")

        else: 
            st.error("Flow Regime: Turbulent")

    engineering_notes( 
        """
        Reynolds Number predicts whether flow is laminar or turbulent. 

        Equation: 
        Re = ρvD/μ

        Flow Classification: 
        Laminar: Re < 2300 
        Transitional: 2300 <= Re <= 4000 
        Turbulent: Re > 4000
        """
        )

    st.caption(
        """
        Engineering Tip: 
        Lower velocity or smaller pipe diameters reduce Reynolds Number, 
        making flow more likely to remain laminar. 
        """
    )

    footer()