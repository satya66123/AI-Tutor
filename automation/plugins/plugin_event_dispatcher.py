class PluginEventDispatcher:

    def __init__(self):

        self.listeners = {}

    def register(
            self,
            event,
            callback
    ):

        self.listeners.setdefault(
            event,
            []
        ).append(callback)

    def dispatch(
            self,
            event,
            plugin
    ):

        callbacks = self.listeners.get(
            event,
            []
        )

        for callback in callbacks:

            callback(plugin)