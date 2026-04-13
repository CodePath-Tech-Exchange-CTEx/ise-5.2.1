import _setup
import streamlit as st
from utils import initialize_logged_in, get_footer, check_login_state, set_header


initialize_logged_in()

set_header("Report")

check_login_state()

st.write(
    """
        Here is a page with a report on it.
    """
)

st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})

st.write(
    """
    Look at those numbers. Amazing.
"""
)

get_footer()
