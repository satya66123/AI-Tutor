import time


class RetryExecutor:

    @staticmethod
    def execute(task_runner, context):

        retries = 0

        policy = task_runner.retry_policy

        while True:

            try:

                return task_runner.execute(context)

            except Exception as ex:

                retries += 1

                if policy is None:

                    raise

                if retries > policy.max_retries:

                    raise

                delay = policy.delay

                if policy.exponential_backoff:

                    delay *= (2 ** (retries - 1))

                time.sleep(delay)