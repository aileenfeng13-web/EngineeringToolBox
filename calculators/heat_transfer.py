import streamlit as st 

def calculate_heat_transfer(k, area, temperature_difference, thickness):
    """
    Calculate conductive heat transfer using Fourier's Law.

    Parameters: 
        k: thermal conductivity (W/m·K)
        area: surface area (m²)
        temperature_difference: temperature difference (K)
        thickness: wall thickness (m)

    Returns: Heat transfer rate (W)
    """
    heat_transfer = (k * area * temperature_difference /thickness)
    return heat_transfer

def show(): 
    st.title("🔥 Heat Transfer Calculator")

    st.write(
        """
        Calculate conductive heat transfer through a flat wall using Fourier's Law.
        """
    )

    k = st.number_input(
        "Thermal Conductivity, k (W/m·K)", 
        value=0.8, 
        min_value=0.0001
    )

    area = st.number_input(
        "Surface Area (m²)", 
        value=10.0, 
        min_value=0.0001
    )

    temperature_difference = st.number_input(
        "Temperature Difference (K)", 
        value=20.0,
        min_value=0.0001
    )

    thickness = st.number_input(
        "Wall Thickness (m)", 
        value=0.1,
        min_value=0.0001
    )

    if st.button("Calculate Heat Transfer"):
        heat_transfer = calculate_heat_transfer(
            k, area, temperature_difference, thickness
        )
        st.success(f"Heat Transfer Rate: {heat_transfer:.2f} W")

        st.info(
            """
            Fourier's Law describes conductive heat transfer through a material. 
            Heat transfer increases with thermal conductivity, surface area, and 
            temperature difference, and decreases as wall thickness increases. 
            """
        )



