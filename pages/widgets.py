import streamlit as st

def hide_toolbar():
    """
    This function removes the toolbar in the streamlit page.
    This ensures that the user can't go between the pages by themselves.
    """
    st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {
        display: none !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)