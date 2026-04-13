import _setup
import streamlit as st
from utils import initialize_logged_in, get_footer, check_login_state, set_header


initialize_logged_in()

set_header("About")

check_login_state()

st.markdown(
    """
    Fake Company LLC Inc. is a fake company created in 2024 for the purposes of making a website with a lot of redundant code.

    It produces nothing and has $0 a year in revenue.

    Usually, companies are not called both "LLC" and "Inc." and must choose one, but this is a fake company so it has both just to be funny.

    Here is a logo that I created with Gemini. It has too many "L"s.
    """
)

st.image("./assets/fake_company.png")

get_footer()
