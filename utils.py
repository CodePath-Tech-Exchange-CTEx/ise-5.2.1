import streamlit as st

def login():
    st.session_state.logged_in = True


def logout():
    st.session_state.logged_in = False

def initialize_logged_in():
    if st.session_state.get("logged_in") == None:
        st.session_state["logged_in"] = False
        
def set_header(title):
    st.set_page_config(page_title=title)

    st.markdown(f"# {title}")
    st.sidebar.header(title)

def check_login_state():
    if st.session_state.logged_in:
        st.sidebar.success("Logged in")
        st.sidebar.button("Log out", key="logout", on_click=logout)
    else:
        st.sidebar.warning("Not logged in")
        st.sidebar.button("Log in", key="login", on_click=login)

    st.sidebar.write("This site is copyright Fake Company LLC Inc., 2024")

def get_footer():
    with st.expander("Company Info"):
        st.write(
            """
            Fake Company LLC Inc. is located at 1600 Amphitheatre Parkway Mountain View, CA 94043
        """
        )

    with st.expander("Links"):
        st.markdown(
            """
            [Google](https://google.com)

            [Gemini](https://gemini.google.com)

            [Streamlit Docs](https://docs.streamlit.io/)
        """
        )