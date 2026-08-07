import streamlit as st 

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
    st.title("🌊 Reynolds Number Calculator")

    st.write(
        """
        Calculate Reynolds Number and determine the flow regime.
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

    with st.expander("Equation Used"): 

        st.latex(
            r"Re=\frac{\rho vD}{\mu}"
        )

        st.write(
            """
            Reynolds Number predicts whether flow is laminar or turbulent. 

            Typical ranges: 
            Laminar: Re < 2300 
            Transitional: 2300 <= Re <= 4000 
            Turbulent: Re > 4000
            """
        )

    st.divider()

    st.caption(
        """
        Engineering Tip: 
        Lower velocity or smaller pipe diameters reduce Reynolds Number, 
        making flow more likely to remain laminar. 
        """
    )