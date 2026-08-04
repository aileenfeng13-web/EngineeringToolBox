import streamlit as st 

from utils.conversions import (
    convert_length, 
    convert_mass
)

def show(): 
    st.title("📏 Unit Converter")
    st.write("Convert between common engineering length units.") 

    category = st.selectbox(
        "Category",
        [
            "Length", 
            "Mass"
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
    else: 
        units = [
            "Kilograms", 
            "Grams", 
            "Pounds"
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

            else: 
                result = convert_mass(
                    value, 
                    from_unit, 
                    to_unit
                )

            st.success(
                f"{value} {from_unit} = {result:.4f} {to_unit}"
            )

    st.caption(
        "Engineering Toolbox v1.0"
    )




