from typing import Callable
import operator as opr

_priorities:dict[str,int] = {'+':0 , '-':0, '/':1, '*':1, '^':2,'(': 0,'[':0}
_operators:dict[str,Callable[[int,int],int]] = {
    '+' : opr.add,
    '-' : opr.sub,
    '*' : opr.mul,
    '/' : opr.truediv,
    '^' : opr.pow,
}

def eval(expr:str) -> int:
    tokens = rpn(expr)
    print(' '.join(tokens))
    stack:list[int] = []
    for token in tokens:
        if token in _operators:
            a = stack.pop()
            b = stack.pop()
            stack.append(_operators[token](b,a))
        else:
            stack.append(int(token))
    return stack[0]



def rpn(expr: str) -> list[str]:
    sep = '+-*/^()'
    for ch in sep:
        expr = expr.replace(ch,f' {ch} ')
    tokens = expr.split(' ')
    res:list[str] = [] # результат
    ops:list[str] = ['['] # stack операторов
    for token in tokens:
        if token == '':
            pass
        elif token in _priorities:
            if _priorities[token] > _priorities[ops[-1]]:
                ops.append(token)
            else:
                while _priorities[ops[-1]] > _priorities[token]:
                    res.append(ops.pop())
                ops.append(token)
        elif token == '(':
            ops.append(token)
        elif token == ')':
            while ops[-1]!='(':
                res.append(ops.pop())
            ops.pop()
        else:
            res.append(token)
    while len(ops) > 1:
        res.append(ops.pop())
    return res


