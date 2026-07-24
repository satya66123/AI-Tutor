from dataclasses import dataclass


@dataclass
class DatabaseConfig:

    host: str = "localhost"

    port: int = 3306

    user: str = "root"

    password: str = ""

    database: str = "ai_tutor"

    pool_size: int = 10