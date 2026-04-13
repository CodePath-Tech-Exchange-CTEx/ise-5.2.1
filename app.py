import streamlit as st
from utils import get_footer, check_login_state, initialize_logged_in

initialize_logged_in()

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to Streamlit!")

check_login_state()

st.markdown(
    """
    This website has a lot of redundant code. Can you find it and create a utility file which contains the redundancies?
    """
)

get_footer()
