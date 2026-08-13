import streamlit as st

from calculators.unit_converter import show as show_unit_converter

from calculators.pipe_flow import show as show_pipe_flow

from calculators.pressure_drop import show as show_pressure_drop

from calculators.heat_transfer import show as show_heat_transfer

from calculators.pipe_sizing import show as show_pipe_sizing

# Page Configuration

st.set_page_config(
    page_title="Engineering Toolbox",
    page_icon="🛠️",
    layout="wide"
)

from calculators.ideal_gas import (
    show as show_ideal_gas
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
        "📉 Pipe Pressure Drop",
        "🔥 Heat Transfer",
        "🔧 Pipe Sizing"
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

    st.header("Avaliable Tools")
    col1, col2 = st.columns(2)

    with col1: 
        st.subheader("🌡️ Thermodynamics")
        st.write(
            """
            Calculate properties of ideal gases using the Ideal Gas Law.
            """
        )
        st.markdown(
            """
            **Avaliable calculations** 
            - Ideal Gas Law 
            - Pressure
            - Volume 
            - Temperature
            - Moles
            """
        )

        with col2:
            st.subheader("🌊 Fluid Mechanics")
            st.write(
                """
                Analyze flow behavior and pressure losses in pipes.
                """
            )
            st.markdown(
                """
                **Avaliable calculations**
                - Reynolds Number 
                - Flow Regime
                - Friction Factor
                - Pressure Drop
                """
            )
        st.divider()

        st.header("Technologies")
        st.write(
            """
            Python • Streamlit • NumPy • Matplotlib • Pytest • Git • GitHub
            """
        )

        st.divider()

        st.header("About This Project")
        st.write(
            """
            This project was created to combine chemical engineering concepts with software development. The calculations are implemented using Python and tested using automated unit tests. 
            """
        )

    st.header("🚀 Current Progress")

    st.checkbox("Home Page", value=True)

    st.checkbox("Unit Converter")

    st.checkbox("Ideal Gas Calculator")

    st.checkbox("Pipe Flow Calculator")

    st.checkbox("Heat Transfer Calculator")

    st.checkbox("Pipe Sizing Calculator")

    st.divider()

    st.header("📖 About")

    st.write(
        """
        This project demonstrates software engineering, Python programming, engineering calculations, and interactive visualization.
        """
    )

    st.caption("Created by Aileen Feng")

elif page == "📏 Unit Converter": 
    show_unit_converter()

elif page == "⚗️ Ideal Gas Law": 
    show_ideal_gas()

elif page == "🌊 Pipe Flow": 
    show_pipe_flow()

elif page == "📉 Pipe Pressure Drop": 
    show_pressure_drop()

elif page == "🔥 Heat Transfer":
    show_heat_transfer

elif page == "🔧 Pipe Sizing": 
    show_pipe_sizing

