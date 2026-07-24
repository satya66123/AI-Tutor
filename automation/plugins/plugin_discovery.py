from pathlib import Path


class PluginDiscovery:

    def __init__(self, plugin_directory):

        self.plugin_directory = Path(plugin_directory)

    def discover(self):

        plugins = []

        for file in self.plugin_directory.glob("*_plugin.py"):

            module = ".".join(file.with_suffix("").parts)

            plugins.append(module)

        return plugins