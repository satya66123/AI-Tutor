import importlib


class PluginLoader:

    @staticmethod
    def load(module_name):

        module = importlib.import_module(module_name)

        return module