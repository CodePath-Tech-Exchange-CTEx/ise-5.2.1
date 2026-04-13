import _setup
import streamlit as st
from utils import initialize_logged_in, get_footer, check_login_state, set_header


initialize_logged_in()

set_header("Overview")

check_login_state()


st.write(
    """Here is a page with a site overview.

    This site has one main page (app) and three pages (about, overview, and report).

    All of them have some redundant code that can be abstracted out to make changes easier in the future.
    """
)

get_footer()
