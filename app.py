import streamlit as st

from calculators.unit_converter import show as show_unit_converter

# Page Configuration

st.set_page_config(
    page_title="Engineering Toolbox",
    page_icon="🛠️",
    layout="wide"
)


# Sidebar

st.sidebar.title("🛠 Engineering Toolbox")

page = st.sidebar.radio(
    "Choose a tool",
    [
        "🏠 Home",
        "📏 Unit Converter",
        "⚗️ Ideal Gas Law",
        "🌊 Pipe Flow",
        "🔥 Heat Transfer"
    ]
)

# HOME PAGE

if page == "🏠 Home":

    st.title("🛠 Engineering Toolbox")

    st.subheader(
        "A collection of engineering calculators built with Python"
    )

    st.write(
        """
        Welcome!

        This project is designed to help engineering students
        perform common calculations while learning the underlying theory.

        Throughout my engineering degree, I'll continue expanding
        this toolbox with new calculators and visualizations.
        """
    )

    st.divider()

    st.header("🚀 Current Progress")

    st.checkbox("Home Page", value=True)

    st.checkbox("Unit Converter")

    st.checkbox("Ideal Gas Calculator")

    st.checkbox("Pipe Flow Calculator")

    st.checkbox("Heat Transfer Calculator")

    st.divider()

    st.header("📖 About")

    st.write(
        """
        This project demonstrates software engineering,
        Python programming, engineering calculations,
        and interactive visualization.
        """
    )

    st.caption("Created by Aileen Feng")

elif page == "📏 Unit Converter": 
    show_unit_converter()

