import random


class Environment:
    def __init__(
        self,
        *,
        color: str | None = None,
        on_color: str | None = None,
        symbol: str = " ",
    ):
        self.__color = color
        self.__on_color = on_color
        self.__symbol = symbol

    @property
    def color(self) -> str | None:
        return self.__color

    @property
    def on_color(self) -> str | None:
        return self.__on_color

    @property
    def symbol(self) -> str:
        return self.__symbol

    def __str__(self) -> str:
        if self.color is None:
            return f"[on {self.on_color}]{self.symbol}[/]"
        elif self.on_color is None:
            return f"[{self.color}]{self.symbol}[/]"
        else:
            return f"[{self.color} on {self.on_color}]{self.symbol}[/]"


class Field:

    forest = Environment(on_color="green4", color="grey37", symbol="*")
    meadow = Environment(on_color="green3")
    mountain = Environment(on_color="grey37", symbol="^")
    water = Environment(on_color="dark_blue")

    def __init__(self, rows: int, cols: int) -> None:
        self.__rows = rows
        self.__cols = cols
        self.environment: list[list[Environment]] = []
        self.GenerateMap()

    @property
    def rows(self) -> int:
        return self.__rows

    @property
    def cols(self) -> int:
        return self.__cols

    def GenerateMap(self) -> None:
        envs = [Field.forest, Field.meadow, Field.mountain, Field.water]
        for i in range(0, self.rows):
            self.environment.append([])
            for j in range(0, self.cols):
                self.environment[i].append(random.choice(envs))
