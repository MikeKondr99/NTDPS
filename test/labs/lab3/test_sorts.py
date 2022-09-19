import pytest
from typing import Tuple, TypeVar
import src.labs.lab3.sorts as sort
from src.labs.lab3.sorts import TNum


def prep(input: list[TNum]) -> Tuple[list[TNum], list[TNum]]:
    return (input, sorted(input))


input1 = [3, 2, 1]
input2 = [45, 15, 75, 37, 14, 86, 12, 53, 53]
input3 = [0.75, 0.234, 0.124, 0.717, 0.363, 0.934]
input4 = [84, -68, -49, -18, 13, 67, 81, 99]
input5 = [
    "Complexity",
    " Equivalent",
    " Fuselage",
    " Keen",
    " Pig farm",
    " Polio",
    " Ratny",
    " Snowman",
    " To",
]


PARAMS = [prep(input1), prep(input2), prep(input3), prep(input4)]


@pytest.mark.parametrize("input,expected", PARAMS)
def test_bubble(input: list[TNum], expected: list[TNum]) -> None:
    assert sort.bubble(input) == expected


@pytest.mark.parametrize("input,expected", PARAMS)
def test_selection(input: list[TNum], expected: list[TNum]) -> None:
    assert sort.selection(input) == expected


@pytest.mark.parametrize("input,expected", PARAMS)
def test_quick(input: list[TNum], expected: list[TNum]) -> None:
    assert sort.quick(input) == expected
