from dataclasses import dataclass

from automation.condition_operator import ConditionOperator


@dataclass
class Condition:

    variable: str

    operator: ConditionOperator

    value: object = None