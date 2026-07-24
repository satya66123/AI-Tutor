from automation.condition_evaluator import ConditionEvaluator


class DependencyResolver:

    @staticmethod
    def ready(step, completed, context):

        if not step.enabled:
            return False

        if not all(dep in completed for dep in step.depends_on):
            return False

        for condition in step.conditions:

            if not ConditionEvaluator.evaluate(
                    condition,
                    context
            ):
                return False

        return True