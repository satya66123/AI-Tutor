class PluginContext:

    def __init__(self):

        self.data = {}

    def set(self,
            key,
            value):

        self.data[key] = value

    def get(self,
            key,
            default=None):

        return self.data.get(
            key,
            default
        )

    def contains(self,
                 key):

        return key in self.data

    def remove(self,
               key):

        if key in self.data:

            del self.data[key]

    def clear(self):

        self.data.clear()