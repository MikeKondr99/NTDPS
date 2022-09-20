import os
import keyboard  # type: ignore
from rich import print
from rich.panel import Panel
from rich.live import Live
from rich.table import Table
from rich.prompt import Prompt
import random
import time
from typing import Tuple
from src.labs.lab2.game import Field, Unit


class GameFieldRenderer:
    def __init__(self, rows: int, cols: int) -> None:
        self.cursor: list[int] = [2, 2]
        self.cursor_visible: bool = False
        self.field: Field = Field(rows, cols)

    def __rich__(self) -> str:
        res = ""
        for x in range(0, self.field.rows):
            for y in range(0, self.field.cols):
                unit = self.field.units[x][y]
                env = self.field.environment[x][y]
                if x == self.cursor[0] and y == self.cursor[1] and self.cursor_visible:
                    if isinstance(unit, Unit):
                        res += f"[on black]{unit.symbol}[/on black]"
                    else:
                        res += f"[on black]{env.symbol}[/on black]"
                else:
                    if isinstance(unit, Unit):
                        res += f"[{unit.color} on {env.on_color}]{unit.symbol}[/]"
                    else:
                        res += str(env)

            res += "\n"
        return res[:-1]

    def run(self) -> None:
        cmd = ""
        while True:
            os.system("cls")
            print(Panel.fit(self.__rich__()), end="")
            cmd = input("> ")
            if cmd == "q":
                break
            if cmd == "r":
                self.field = Field(self.field.rows, self.field.cols)
                continue
            self.cursor_visible = True
            while True:
                if keyboard.is_pressed("a"):
                    self.cursor[1] = max(0, self.cursor[1] - 1)
                    os.system("cls")
                    print(Panel.fit(self.__rich__()), end="")
                elif keyboard.is_pressed("d"):
                    self.cursor[1] = min(self.field.rows - 1, self.cursor[1] + 1)
                    os.system("cls")
                    print(Panel.fit(self.__rich__()), end="")
                elif keyboard.is_pressed("w"):
                    self.cursor[0] = max(0, self.cursor[0] - 1)
                    os.system("cls")
                    print(Panel.fit(self.__rich__()), end="")
                elif keyboard.is_pressed("s"):
                    self.cursor[0] = min(self.field.cols - 1, self.cursor[0] + 1)
                    os.system("cls")
                    print(Panel.fit(self.__rich__()), end="")
                elif keyboard.is_pressed("f"):
                    keyboard.press_and_release("enter")
                    input()
                    break
                time.sleep(0.1)
            self.cursor_visible = False
        return
