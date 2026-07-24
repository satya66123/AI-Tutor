from dataclasses import dataclass, field


@dataclass
class PluginConfig:

    enabled: bool = True

    auto_load: bool = True

    version: str = "1.0.0"

    settings: dict = field(
        default_factory=dict
    )