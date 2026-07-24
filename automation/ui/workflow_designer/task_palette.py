import streamlit as st

from automation.task_registry import TaskRegistry


class TaskPalette:

    @staticmethod
    def render():

        st.subheader("Task Palette")

        tasks = TaskRegistry.list_tasks()

        selected = st.selectbox(

            "Available Tasks",

            tasks,

            key="palette_task"

        )

        add = st.button(

            "➕ Add Step",

            use_container_width=True

        )

        return selected, add