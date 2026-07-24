from enum import Enum


class PluginLifecycle(Enum):

    CREATED = "CREATED"

    LOADED = "LOADED"

    INITIALIZED = "INITIALIZED"

    RUNNING = "RUNNING"

    STOPPED = "STOPPED"

    UNLOADED = "UNLOADED"

    FAILED = "FAILED"