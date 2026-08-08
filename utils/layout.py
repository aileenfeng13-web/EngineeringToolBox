import streamlit as st 

def page_header(title, description): 
    """
    Creates a consistent page header
    """

    st.title(title) 

    st.write(description) 

    st.divider()

def engineering_notes(notes):
    """
    Creates a collapsible engineering notes section.
    """
    with st.expander("Engineering Notes"): 
        st.write(notes) 

def footer(): 
    """
    Creates application footer
    """
    st.divider()

    st.caption(
        "Engineering Toolbox | Built with Python and Streamlit"
    )