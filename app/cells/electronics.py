# Third-party modules
from sympy import *

# Python native modules
from enum import Enum

import math


# ---------------- #
# Type Definitions #
# ---------------- #
class ComponentType(Enum):
    Resistor = "Resistor"
    Capacitor = "Capacitor"


# --------------------------- #
# Constant Values Declaration #
# --------------------------- #
COMMERCIAL_RESISTORS = [
    1, 1.1, 1.2, 1.3, 1.5, 1.8, 2, 2.2, 2.4, 2.7, 3, 3.3, 3.6, 3.9, 4.3, 4.7, 5.1,
    5.6, 6.2, 6.8, 7.5, 8.2, 9.1
]

MULTIPLIER_RESISTORS = [10e0, 10e1, 10e2, 10e3, 10e4, 10e5]

COMMERCIAL_CAPACITORS = [
    1, 1.2, 1.5, 1.8, 2.2, 2.7, 3.3, 3.9, 4.7, 5.6, 6.8, 8.2
]

MULTIPLER_CAPACITORS = [1e-12, 10e-12, 100e-12, 1e-9, 10e-9, 100e-9, 1e-6]


# ---------------- #
# Public Functions #
# ---------------- #
def compute_commercial_values(component_type: ComponentType) -> list:
    """ Returns a list of possible commercial values for the given component type.
    Returns None if non-identified component type. """

    def multiply_lists(first_list, second_list) -> list:
        new_list = []
        for first_element in first_list:
            for second_element in second_list:
                new_list.append(first_element * second_element)
        return new_list

    if component_type is ComponentType.Resistor:
        return multiply_lists(MULTIPLIER_RESISTORS, COMMERCIAL_RESISTORS)
    elif component_type is ComponentType.Capacitor:
        return multiply_lists(MULTIPLER_CAPACITORS, COMMERCIAL_CAPACITORS)
    else:
        return None


def compute_commercial_by_iteration(
        element_one: ComponentType, element_two: ComponentType,
        callback: callable, error: float,
        fixed_one_values=None,
        fixed_two_values=None) -> list:
    """ Returns [(element_one_value, element_two_value)], list of 2-tuple with possible values
    that verify the expression element_one = element_two * k, with a relative decimal expressed error.
    Fixed list of values can be used to process the iteration.
    """
    # Loading possible choices for each element, setting up the result list
    element_one_values = compute_commercial_values(element_one) if fixed_one_values is None else fixed_one_values
    element_two_values = compute_commercial_values(element_two) if fixed_two_values is None else fixed_two_values
    results = []

    # Find for each possible element_two value, a resulting element_one and verify
    # if matches with a commercial value with the given error tolerance
    for element_two_value in element_two_values:
        element_one_target = callback(element_two_value)

        for element_one_value in element_one_values:
            if math.isclose(element_one_target, element_one_value, rel_tol=error):
                results.append((element_one_value, element_two_value))

    # Returning the results... empty or not
    return results


# ----------------------- #
# Standard callback tools #
# ----------------------- #
def build_expression_callback(expression, target, symbol):
    """ Returns a callback to get the element_one as function of element_two,
    by solving an equation for the expression = target, getting the given symbol. """
    solutions = solve(Eq(expression, target), symbol)
    symbol_expression = solutions[0]

    def callback(element_two_value: float):
        symbol = symbol_expression.free_symbols.pop()
        symbol_expression.free_symbols.add(symbol)
        return symbol_expression.evalf(subs={symbol: element_two_value})
    return callback


def build_proportional_callback(k: float):
    """ Returns a callback which operates as element_one = element_two * k """
    def callback(element_two_value: float):
        return element_two_value * k
    return callback