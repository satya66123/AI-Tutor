"""
Settings Validator
"""


class SettingsValidator:

    @staticmethod
    def validate_temperature(value):

        return 0 <= value <= 2

    @staticmethod
    def validate_tokens(value):

        return value > 0