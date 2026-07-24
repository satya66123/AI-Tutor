class PluginRegistry:

    def __init__(self):

        self.plugins = {}

    def register(self, plugin):

        self.plugins[plugin.name] = plugin

    def unregister(self, plugin_name):

        if plugin_name in self.plugins:

            del self.plugins[plugin_name]

    def get(self, plugin_name):

        return self.plugins.get(plugin_name)

    def all(self):

        return list(self.plugins.values())

    def enabled(self):

        return [

            plugin

            for plugin in self.plugins.values()

            if plugin.enabled

        ]