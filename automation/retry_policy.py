from dataclasses import dataclass


@dataclass
class RetryPolicy:

    max_retries: int = 3

    delay: float = 1.0

    exponential_backoff: bool = True

    retry_on_exception: bool = True