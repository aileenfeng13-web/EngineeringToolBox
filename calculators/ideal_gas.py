from utils.constants import IDEAL_GAS_CONSTANT 
from utils.layout import (
    page_header, 
    engineering_notes, 
    footer
)

def calculate_pressure(
        volume, 
        moles, 
        temperature
):
    """
    Calculates pressure using the ideal gas law
    PV = nRT
    Returns pressure in Pascals
    """
    pressure = (
        moles * 
        IDEAL_GAS_CONSTANT * 
        temperature
    ) / volume 

    return pressure 

import streamlit as st 

def show():

    page_header(
        "⚗️ Ideal Gas Law", 
        "Solve PV =nRT by selecting the unknown variable.")

    volume = st.number_input(
        "Volume (m³)", 
        value = 1.0, 
        min_value = 0.0001
    )

    moles = st.number_input(
        "Number of moles (mol)", 
        value = 1.0
    )

    temperature = st.number_input(
        "Temperature (K)", 
        value = 298.15   
    )
    
    if st.button("Calculate Pressure"): 
        if volume <= 0:
            st.error("Volume must be greater than zero.")

        elif temperature <= 0: 
            st.error("Temperature must be above 0 Kelvin")

        else: 
            pressure = calculate_pressure(
                volume, 
                moles, 
                temperature
            )

            st.success("Calculation Complete")

            st.metric(
                "Pressure", 
                f"{pressure:.2f} Pa"
            )

            engineering_notes(

                """
                Equation: 
                
                P = nRT / V 
                
                where: 

                P = Pressure 
                V = Volume
                n = Moles 
                R = Ideal Gas Constant 
                T = Temperature

                Assumptions: 
                - Gas behaves ideally 
                - Pressure is measured in Pascals 
                - Volume is measured in cubic meters 
                - Temperature is measured in Kelvin
                """
                
                )
            footer()