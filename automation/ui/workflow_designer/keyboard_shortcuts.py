import streamlit as st


class KeyboardShortcuts:

    @staticmethod
    def render():

        with st.expander("⌨ Keyboard Shortcuts", expanded=False):

            shortcuts = [
                ("Ctrl + N", "New Workflow"),
                ("Ctrl + S", "Save Workflow"),
                ("Ctrl + O", "Open Workflow"),
                ("Ctrl + E", "Execute Workflow"),
                ("Delete", "Delete Selected Step"),
                ("Ctrl + ↑", "Move Step Up"),
                ("Ctrl + ↓", "Move Step Down"),
                ("Ctrl + Shift + C", "Clear Workflow"),
                ("Esc", "Cancel Selection")
            ]

            st.markdown("### Available Shortcuts")

            for key, action in shortcuts:

                c1, c2 = st.columns([2, 5])

                with c1:
                    st.code(key)

                with c2:
                    st.write(action)