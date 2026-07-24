import streamlit as st


class Toolbar:

    @staticmethod
    def render():

        col1, col2, col3, col4 = st.columns(4)

        new = False
        save = False
        execute = False
        clear = False

        with col1:

            new = st.button(
                "New"
            )

        with col2:

            save = st.button(
                "Save"
            )

        with col3:

            execute = st.button(
                "Execute"
            )

        with col4:

            clear = st.button(
                "Clear"
            )

        return {

            "new": new,

            "save": save,

            "execute": execute,

            "clear": clear

        }