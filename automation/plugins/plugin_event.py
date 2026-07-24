from enum import Enum


class PluginEvent(Enum):

    LOAD = "LOAD"

    INITIALIZE = "INITIALIZE"

    EXECUTE = "EXECUTE"

    SHUTDOWN = "SHUTDOWN"

    ERROR = "ERROR"