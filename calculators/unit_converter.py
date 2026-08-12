import streamlit as st 

from utils.conversions import (
    convert_length, 
    convert_mass, 
    convert_temperature
)

def show(): 
    st.title("📏 Unit Converter")
    st.write("Convert between common engineering length units.") 

    category = st.selectbox(
        "Category",
        [
            "Length", 
            "Mass", 
            "Temperature"
        ]
    )

    value = st.number_input(
        "Enter a value:",
        value=1.0,
        step=0.1
    )

    if category == "Length": 
        units = [
            "Meters", 
            "Centimeters", 
            "Milimeters", 
            "Kilometers", 
            "Inches", 
            "Feet"

        ]
    elif category == "Mass": 
        units = [
            "Kilograms", 
            "Grams", 
            "Pounds"
        ]

    elif category == "Temperature": 
        units = [
            "Celsius", 
            "Fahrenheit", 
            "Kelvin"
        ]

    from_unit = st.selectbox(
        "From", 
        units
    )

    to_unit = st.selectbox(
        "To", 
        units
    )
    st.divider()

    if st.button("Convert"):

        if from_unit == to_unit:

            st.info(
            "The input and output units are the same."
            )

        else:

            if category == "Length": 

                result = convert_length(
                    value,
                    from_unit,
                    to_unit
                )

            elif category == "Mass": 
                result = convert_mass(
                    value, 
                    from_unit, 
                    to_unit
                )

            elif category == "Temperature":
                result = convert_temperature(
                    value, 
                    from_unit, 
                    to_unit
                )

            st.success("Conversion Complete!")

            st.metric(
                label = "Result", 
                value = f"{result:.4f} {to_unit}"
            )
            
        with st.expander("Engineering Notes"):
            st.write(
                """
                - Length conversions use meters as the base unit.
                - Mass conversions use kilograms as the base unit.
                - Temperature conversions use celsius as the intermediate unit.
                """)

    st.caption(
        "Engineering Toolbox v1.0"
    )




