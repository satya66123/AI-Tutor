"""
Response Time Service
"""

import time


class ResponseTimeService:

    @staticmethod
    def start():

        return time.perf_counter()

    @staticmethod
    def stop(start):

        end = time.perf_counter()

        return round((end - start) * 1000, 2)