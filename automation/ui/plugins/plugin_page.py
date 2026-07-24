import pandas as pd
import streamlit as st


class PluginPage:

    def __init__(self, manager):

        self.manager = manager

    def render(self):

        st.title("Plugin Manager")

        plugins = []

        for plugin in self.manager.plugins():

            plugins.append({

                "Name": plugin.name,

                "Version": plugin.version,

                "Enabled": plugin.enabled,

                "Lifecycle": plugin.lifecycle.value,

                "Author": plugin.author

            })

        st.dataframe(

            pd.DataFrame(plugins),

            use_container_width=True

        )