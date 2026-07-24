from automation.condition_operator import ConditionOperator


class ConditionEvaluator:

    @staticmethod
    def evaluate(condition, context):

        current = context.get(condition.variable)

        match condition.operator:

            case ConditionOperator.EQUAL:
                return current == condition.value

            case ConditionOperator.NOT_EQUAL:
                return current != condition.value

            case ConditionOperator.GREATER_THAN:
                return current > condition.value

            case ConditionOperator.GREATER_EQUAL:
                return current >= condition.value

            case ConditionOperator.LESS_THAN:
                return current < condition.value

            case ConditionOperator.LESS_EQUAL:
                return current <= condition.value

            case ConditionOperator.EXISTS:
                return context.contains(condition.variable)

            case ConditionOperator.NOT_EXISTS:
                return not context.contains(condition.variable)

        return False