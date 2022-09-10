from typing import Callable
import operator as opr
import math

_priorities: dict[str, int] = {
    "+": 0,
    "-": 0,
    "/": 1,
    "*": 1,
    "^": 2,
    "(": -1,
    "": -1,
    "u+": 5,
    "u-": 5,
}
_unary: set[str] = {"+", "-"}
_operators: dict[str, Callable[[float, float], float]] = {
    "+": opr.add,
    "-": opr.sub,
    "*": opr.mul,
    "/": opr.truediv,
    "^": opr.pow,
}
_unary_operators: dict[str, Callable[[float], float]] = {
    "u+": lambda x: x,
    "u-": lambda x: -x,
}

_variables: dict[str, float] = {
    "pi": math.pi,
    "e": math.e,
    "tau": math.tau,
}


def eval(expr: str) -> float:
    try:
        tokens = rpn(expr)
    except Exception as e:
        raise e
    stack: list[float] = []
    for token in tokens:
        if token in _operators:
            a = stack.pop()
            b = stack.pop()
            try:
                stack.append(_operators[token](b, a))
            except ZeroDivisionError:
                raise Exception("Деление на ноль")
        elif token in _unary_operators:
            a = stack.pop()
            stack.append(_unary_operators[token](a))
        else:
            if token in _variables:
                stack.append(_variables[token])
            elif token.isdigit():
                stack.append(float(token))
            else:
                raise Exception(f"Неизвестный операнд '{token}'")
    return stack[0]


def rpn(expr: str) -> list[str]:
    if not expr.strip():
        raise Exception("Пустая строка")
    sep = "+-*/^()"
    for ch in sep:
        expr = expr.replace(ch, f" {ch} ")
    tokens = expr.split(" ")
    plevel = 0  # уровень вложенности скобок
    operand = True  # сейчас ожидается операнд
    res: list[str] = []  # результат
    ops: list[str] = [""]  # stack операторов
    for token in tokens:
        if token == "":
            pass
        elif token == "(":
            if not operand:
                raise Exception(f"Ожидался оператор, вместо '{token}'")
            ops.append(token)
            plevel += 1
            operand = True
        elif token in _priorities:  # обработка операций
            if operand:
                if token in _unary:
                    token = "u" + token
                else:
                    raise Exception(f"Ожидался операнд, вместо '{token}'")
            if _priorities[token] > _priorities[ops[-1]] or (
                token == "^" and ops[-1] == "^"
            ):
                ops.append(token)
            else:
                while _priorities[ops[-1]] >= _priorities[token]:
                    res.append(ops.pop())
                ops.append(token)
            operand = True
        elif token == ")":
            if operand:
                raise Exception(f"Ожидался операнд, вместо '{token}'")
            while ops[-1] != "(" and ops[-1] != "":
                res.append(ops.pop())
            if ops[-1] == "":
                raise Exception("Лишняя закрывающая скобка")
            else:
                ops.pop()
                plevel -= 1
            operand = False
        else:
            if not operand:
                raise Exception(f"Ожидался оператор, вместо '{token}'")
            res.append(token)
            operand = False
    if plevel > 0:
        raise Exception("Скобка не была закрыта")
    if operand:
        raise Exception("Ожидался операнд в конце")

    while len(ops) > 1:
        res.append(ops.pop())
    return res
