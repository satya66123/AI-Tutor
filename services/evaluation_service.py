"""
Enterprise Evaluation Service
"""

import time


class EvaluationService:

    @staticmethod
    def evaluate(function):

        start = time.time()

        result = function()

        end = time.time()

        return {

            "result": result,

            "latency_ms": round(
                (end - start) * 1000,
                2
            )

        }