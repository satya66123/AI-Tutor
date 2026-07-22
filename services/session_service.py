"""
Session Service
"""

import uuid


class SessionService:

    @staticmethod
    def create():

        return str(uuid.uuid4())