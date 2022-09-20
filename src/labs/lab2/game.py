import random
from perlin_noise import PerlinNoise  # type: ignore


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


# base \u25D9
class Unit:
    def __init__(self, symbol: str, color: str):
        self.__color = color
        self.__symbol = symbol

    @property
    def color(self) -> str | None:
        return self.__color

    @property
    def symbol(self) -> str:
        return self.__symbol


class Field:
    forest = Environment(on_color="green4", color="grey37", symbol="\uF1BB")
    meadow = Environment(on_color="green3")
    flower = Environment(on_color="green3", color="indian_red", symbol="*")
    flower2 = Environment(on_color="green3", color="yellow", symbol="*")
    flower3 = Environment(on_color="green3", color="cyan", symbol="*")
    mountain = Environment(on_color="grey37", symbol="^")
    water = Environment(on_color="blue", symbol="≈", color="bright_blue")

    def __init__(self, rows: int, cols: int) -> None:
        self.__rows = rows
        self.__cols = cols
        self.environment: list[list[Environment]] = []
        self.units: list[list[Unit | None]] = []
        for i in range(0, self.rows):
            self.units.append([])
            for j in range(0, self.cols):
                self.units[i].append(None)
        self.units[i][j] = Unit("B", "white")
        self.GenerateMap()

    @property
    def rows(self) -> int:
        return self.__rows

    @property
    def cols(self) -> int:
        return self.__cols

    def GenerateMap(self) -> None:
        river = PerlinNoise(0.5, random.randint(1, 1000))
        mountain = PerlinNoise(0.5, random.randint(1, 1000))
        forest = PerlinNoise(4, random.randint(1, 1000))
        flowers = PerlinNoise(7, random.randint(1, 1000))
        for i in range(0, self.rows):
            self.environment.append([])
            for j in range(0, self.cols):
                self.environment[i].append(Field.meadow)
        for i in range(0, self.rows):
            for j in range(0, self.cols):
                # Леса
                val4 = flowers([i / self.rows, j / self.cols])
                if val4 > 0.14:
                    self.environment[i][j] = random.choice(
                        [Field.flower, Field.flower2, Field.flower3]
                    )
                # Леса
                val3 = forest([i / self.rows, j / self.cols])
                if val3 > 0.14:
                    self.environment[i][j] = Field.forest
                # Горы
                val2 = mountain([i / self.rows, j / self.cols])
                if val2 > 0.16 and val2 < 0.20:
                    self.environment[i][j] = Field.mountain
                # Реки
                val = river([i / self.rows, j / self.cols])
                if val > 0.15 and val < 0.20:
                    self.environment[i][j] = Field.water
