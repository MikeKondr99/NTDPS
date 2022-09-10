import pytest
import math
import src.labs.lab1.my_calc as calc
from typing import Tuple


def _test(expr: str, rpn: str, answer: str | float | None = None) -> None:
    if answer is None:
        with pytest.raises(Exception) as context:
            calc.rpn(expr)
        assert rpn == str(context.value)
        with pytest.raises(Exception) as context:
            calc.eval(expr)
        assert rpn == str(context.value)
    else:
        assert rpn == " ".join(calc.rpn(expr))
        if isinstance(answer, str):
            with pytest.raises(Exception) as context:
                calc.eval(expr)
            assert answer == str(context.value)
        elif isinstance(answer, float):
            assert calc.eval(expr) == pytest.approx(answer)


def test_eval_one_number() -> None:
    _test("42", "42", 42)


def test_eval_variables() -> None:
    _test("e", "e", math.e)
    _test("pi", "pi", math.pi)
    _test("tau", "tau", math.tau)


def test_eval_two() -> None:
    _test("42 + 12", "42 12 +", 42 + 12)
    _test("42 * 12", "42 12 *", 42 * 12)
    _test("42 - 12", "42 12 -", 42 - 12)
    _test("42 / 12", "42 12 /", 42 / 12)
    _test("42 ^ 2", "42 2 ^", 42**2)


def test_priority() -> None:
    _test("2 + 2 * 2", "2 2 2 * +", 6)
    _test("2 + 2 ^ 3", "2 2 3 ^ +", 10)
    _test("2 + 2 / 3", "2 2 3 / +", 2.666666666666666666666)
    _test("5 + 4 * 3 ^ 2", "5 4 3 2 ^ * +", 41)


def test_parentheses() -> None:
    _test("(2 + 2) * 2", "2 2 + 2 *", 8)
    _test("(2 + 2) ^ 3", "2 2 + 3 ^", 4**3)
    _test("(2 + 2) / 3", "2 2 + 3 /", 4 / 3)
    _test("((5 + 4) * 3) ^ 2", "5 4 + 3 * 2 ^", 27**2)
    _test("((5 + 4) * 3) ^ 2", "5 4 + 3 * 2 ^", 27**2)


def test_bracket_not_closed() -> None:
    _test("(2 + 2", "Скобка не была закрыта")


def test_bracket_more_closed() -> None:
    _test("2 + 2)", "Лишняя закрывающая скобка")


def test_unary_plus() -> None:
    _test("2 + + 2", "2 2 u+ +", 4)


def test_unary_minus() -> None:
    _test("2 + - 3", "2 3 u- +", -1)


def test_double_operator() -> None:
    _test("2 * * 2", "Ожидался операнд, вместо '*'")


def test_operator_at_end() -> None:
    _test("1 + 3 + 5 +", "Ожидался операнд в конце")


def test_division_by_zero() -> None:
    _test("1/0", "1 0 /", "Деление на ноль")


def test_incorrect_operand() -> None:
    _test("a", "a", "Неизвестный операнд 'a'")


def test_left_sub() -> None:
    _test("2 - 3 - 4", "2 3 - 4 -", 2 - 3 - 4)


def test_left_div() -> None:
    _test("2 / 3 / 4", "2 3 / 4 /", 2 / 3 / 4)


def test_right_pow() -> None:
    _test("3 ^ 3 ^ 3", "3 3 3 ^ ^", 3 ** (3**3))


def test_empty_string() -> None:
    _test("", "Пустая строка")
    _test("   \t  ", "Пустая строка")
