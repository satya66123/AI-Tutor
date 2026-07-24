from enum import Enum


class ConditionOperator(Enum):

    EQUAL = "=="

    NOT_EQUAL = "!="

    GREATER_THAN = ">"

    GREATER_EQUAL = ">="

    LESS_THAN = "<"

    LESS_EQUAL = "<="

    EXISTS = "exists"

    NOT_EXISTS = "not_exists"