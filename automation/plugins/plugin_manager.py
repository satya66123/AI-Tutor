from automation.plugins.plugin_loader import PluginLoader
from automation.plugins.plugin_registry import PluginRegistry
from automation.plugins.plugin_lifecycle import PluginLifecycle
from automation.plugins.plugin_discovery import PluginDiscovery


class PluginManager:

    def __init__(self):

        self.loader = PluginLoader()

        self.registry = PluginRegistry()

        self.discovery = PluginDiscovery(
            "automation/plugins/builtin"
        )

    # ----------------------------------------------------
    # Load Plugin
    # ----------------------------------------------------

    def load_plugin(self, module_name):

        module = self.loader.load(module_name)

        plugin = module.Plugin()

        # Prevent duplicate loading
        existing = self.registry.get(plugin.name)

        if existing:
            return existing

        try:

            plugin.lifecycle = PluginLifecycle.LOADED

            plugin.initialize()

            plugin.lifecycle = PluginLifecycle.INITIALIZED

            self.registry.register(plugin)

            return plugin

        except Exception:

            plugin.lifecycle = PluginLifecycle.FAILED

            raise

    # ----------------------------------------------------
    # Load All Plugins
    # ----------------------------------------------------

    def load_all(self):

        modules = self.discovery.discover()

        for module in modules:

            try:

                self.load_plugin(module)

            except Exception as e:

                print(
                    f"Failed to load plugin {module}: {e}"
                )

    # ----------------------------------------------------
    # Execute Plugin
    # ----------------------------------------------------

    def execute_plugin(
            self,
            plugin_name,
            context
    ):

        plugin = self.registry.get(plugin_name)

        if plugin is None:

            raise ValueError(

                f"Plugin '{plugin_name}' not found."

            )

        if not plugin.enabled:

            raise ValueError(

                f"Plugin '{plugin_name}' is disabled."

            )

        try:

            plugin.lifecycle = PluginLifecycle.RUNNING

            result = plugin.execute(context)

            plugin.lifecycle = PluginLifecycle.INITIALIZED

            return result

        except Exception:

            plugin.lifecycle = PluginLifecycle.FAILED

            raise

    # ----------------------------------------------------
    # Unload Plugin
    # ----------------------------------------------------

    def unload_plugin(
            self,
            plugin_name
    ):

        plugin = self.registry.get(plugin_name)

        if plugin is None:

            return False

        try:

            plugin.shutdown()

            plugin.lifecycle = PluginLifecycle.UNLOADED

            self.registry.unregister(plugin_name)

            return True

        except Exception:

            plugin.lifecycle = PluginLifecycle.FAILED

            raise

    # ----------------------------------------------------
    # Reload Plugin
    # ----------------------------------------------------

    def reload_plugin(
            self,
            plugin_name
    ):

        plugin = self.registry.get(plugin_name)

        if plugin is None:

            return None

        module_name = plugin.__class__.__module__

        self.unload_plugin(plugin_name)

        return self.load_plugin(module_name)

    # ----------------------------------------------------
    # Shutdown All
    # ----------------------------------------------------

    def shutdown_all(self):

        for plugin in self.registry.all():

            try:

                plugin.shutdown()

                plugin.lifecycle = PluginLifecycle.UNLOADED

            except Exception:

                plugin.lifecycle = PluginLifecycle.FAILED

        self.registry.plugins.clear()

    # ----------------------------------------------------
    # Enable Plugin
    # ----------------------------------------------------

    def enable(
            self,
            plugin_name
    ):

        plugin = self.registry.get(plugin_name)

        if plugin:

            plugin.enabled = True

            return True

        return False

    # ----------------------------------------------------
    # Disable Plugin
    # ----------------------------------------------------

    def disable(
            self,
            plugin_name
    ):

        plugin = self.registry.get(plugin_name)

        if plugin:

            plugin.enabled = False

            return True

        return False

    # ----------------------------------------------------
    # Get Plugin
    # ----------------------------------------------------

    def get_plugin(
            self,
            plugin_name
    ):

        return self.registry.get(plugin_name)

    # ----------------------------------------------------
    # Is Loaded
    # ----------------------------------------------------

    def is_loaded(
            self,
            plugin_name
    ):

        return self.registry.get(plugin_name) is not None

    # ----------------------------------------------------
    # List Plugins
    # ----------------------------------------------------

    def plugins(self):

        return self.registry.all()

    # ----------------------------------------------------
    # Enabled Plugins
    # ----------------------------------------------------

    def enabled_plugins(self):

        return self.registry.enabled()

    # ----------------------------------------------------
    # Disabled Plugins
    # ----------------------------------------------------

    def disabled_plugins(self):

        return [

            plugin

            for plugin in self.registry.all()

            if not plugin.enabled

        ]

    # ----------------------------------------------------
    # Plugin Count
    # ----------------------------------------------------

    def plugin_count(self):

        return len(

            self.registry.all()

        )

    # ----------------------------------------------------
    # Enabled Plugin Count
    # ----------------------------------------------------

    def enabled_plugin_count(self):

        return len(

            self.registry.enabled()

        )