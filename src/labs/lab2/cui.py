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


class GameFieldRenderer:
    def __init__(self, rows: int, cols: int) -> None:
        self.rows = rows
        self.cols = cols
        self.cursor: list[int] = [2, 2]
        self.cursor_visible: bool = False
        self.field: list[list[MockUnit]] = []
        for i in range(0, rows):
            self.field.append([])
            for j in range(0, cols):
                self.field[i].append(MockUnit())

    def __rich__(self) -> str:
        res = ""
        for x in range(0, self.rows):
            for y in range(0, self.cols):
                if x == self.cursor[0] and y == self.cursor[1]:
                    res += "[on black]" + str(self.field[x][y]) + "[/on black]"
                else:
                    res += self.field[x][y].__rich__()
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
            self.cursor_visible = True
            while True:
                if keyboard.is_pressed("a"):
                    self.cursor[1] = max(0, self.cursor[1] - 1)
                    os.system("cls")
                    print(Panel.fit(self.__rich__()), end="")
                elif keyboard.is_pressed("d"):
                    self.cursor[1] = min(self.rows - 1, self.cursor[1] + 1)
                    os.system("cls")
                    print(Panel.fit(self.__rich__()), end="")
                elif keyboard.is_pressed("w"):
                    self.cursor[0] = max(0, self.cursor[0] - 1)
                    os.system("cls")
                    print(Panel.fit(self.__rich__()), end="")
                elif keyboard.is_pressed("s"):
                    self.cursor[0] = min(self.cols - 1, self.cursor[0] + 1)
                    os.system("cls")
                    print(Panel.fit(self.__rich__()), end="")
                elif keyboard.is_pressed("f"):
                    keyboard.press_and_release("enter")
                    input()
                    break
                time.sleep(0.1)
            self.cursor_visible = False
        return


class MockUnit:
    def __init__(self) -> None:
        self.char: str = " "
        self.color: str | None = None
        self.oncolor: str | None = None
        if random.randrange(1, 100) < 10:
            self.char = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
            self.color = random.choice(
                ["white", "black"],
            )
            self.oncolor = random.choice(["green", "grey37", "dark_blue"])
        else:
            (self.char, self.color, self.oncolor) = random.choice(
                [
                    (" ", "blue", "green"),
                    (" ", "grey69", "grey37"),
                    (" ", "blue", "dark_blue"),
                ]
            )

    def __rich__(self) -> str:
        if self.color is not None:
            if self.oncolor is not None:
                return f"[{self.color} on {self.oncolor}]{self.char}[/]"
            else:
                return f"[{self.color}]{self.char}[/]"
        else:
            return self.char

    def __str__(self) -> str:
        return self.char
