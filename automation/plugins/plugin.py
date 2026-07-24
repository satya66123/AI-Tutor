from abc import ABC, abstractmethod

from automation.plugins.plugin_lifecycle import PluginLifecycle


class Plugin(ABC):

    def __init__(self):

        self.name = ""

        self.version = "1.0.0"

        self.description = ""

        self.author = ""

        self.enabled = True

        self.lifecycle = PluginLifecycle.CREATED

    @abstractmethod
    def initialize(self):
        pass

    @abstractmethod
    def execute(self, context):
        pass

    @abstractmethod
    def shutdown(self):
        pass