import random
import pytest
from pytest_benchmark.fixture import BenchmarkFixture  # type:ignore
from typing import Tuple, TypeVar, Callable
import src.labs.lab3.sorts as sort
from src.labs.lab3.sorts import TNum

random.seed(0x1C2C6D66)

SortingAlgorithm = Callable[[list[TNum]], list[TNum]]
TestData = Tuple[list[TNum], list[TNum]]

SIZES = [10, 1000, 5000]


def prep(input: list[TNum]) -> TestData:
    return (input, sorted(input))


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
    " Rat",
    " Snowman",
    " To",
]
input6: list[int] = []
input7 = [1]


PARAMS = [prep(input2), prep(input3), prep(input4),
          prep(input5), prep(input6), prep(input7)]


@pytest.mark.parametrize("input,expected", PARAMS)
def test_bubble(input: list[TNum], expected: list[TNum]) -> None:
    assert sort.bubble(input) == expected


@pytest.mark.parametrize("input,expected", PARAMS)
def test_selection(input: list[TNum], expected: list[TNum]) -> None:
    assert sort.selection(input) == expected


@pytest.mark.parametrize("input,expected", PARAMS)
def test_quick(input: list[TNum], expected: list[TNum]) -> None:
    assert sort.quick(input) == expected


SIZES = [10, 100, 500, 1000, 1500, 2000, 3000, 4000, 5000, 7500, 10000]
ALGORITHMS = [sort.bubble, sort.selection, sort.quick]


@pytest.mark.parametrize("size", SIZES)
@pytest.mark.parametrize("algorithm", ALGORITHMS)
def test_bench_sort(benchmark, size: int, algorithm: SortingAlgorithm) -> None:  # type: ignore
    data = [random.randint(-10000, 10000) for i in range(0, size)]
    result = benchmark(algorithm, data)
    assert result == sorted(data)
