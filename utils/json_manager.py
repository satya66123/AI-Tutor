"""
JSON Manager
"""

import json
from pathlib import Path


class JsonManager:

    DATA_DIR = Path("data")
    DATA_DIR.mkdir(exist_ok=True)

    @staticmethod
    def save(filename, data):

        filepath = JsonManager.DATA_DIR / filename

        with open(filepath, "w", encoding="utf-8") as file:

            json.dump(
                data,
                file,
                indent=4
            )

    @staticmethod
    def load(filename, default=None):

        filepath = JsonManager.DATA_DIR / filename

        if not filepath.exists():

            return default

        with open(filepath, "r", encoding="utf-8") as file:

            return json.load(file)