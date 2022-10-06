from src.labs.lab2 import Field, Pos
from typing import Callable, Any


class Unit:

    def __init__(self, symbol: str, color: str, actions: dict[str, Callable[[Field, Any, Pos, Pos], str]] = {}):
        self.__color = color
        self.__symbol = symbol
        self.__action = actions

    @property
    def color(self) -> str | None:
        return self.__color

    @property
    def symbol(self) -> str:
        return self.__symbol
