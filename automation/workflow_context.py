from dataclasses import dataclass, field
from threading import RLock
from typing import Any


@dataclass
class WorkflowContext:

    workflow_id: str

    variables: dict[str, Any] = field(default_factory=dict)

    _lock: RLock = field(default_factory=RLock, init=False, repr=False)

    def set(self, key, value):
        with self._lock:
            self.variables[key] = value

    def get(self, key, default=None):
        with self._lock:
            return self.variables.get(key, default)

    def contains(self, key):
        with self._lock:
            return key in self.variables

    def remove(self, key):
        with self._lock:
            self.variables.pop(key, None)

    def clear(self):
        with self._lock:
            self.variables.clear()