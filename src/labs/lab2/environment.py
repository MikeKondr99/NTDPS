
class Environment:

    def __init__(
        self,
        *,
        color: str | None = None,
        on_color: str | None = None,
        symbol: str = " ",
        defense: int = 0
    ) -> None:
        self.__color = color
        self.__on_color = on_color
        self.__symbol = symbol
        self.__defense = defense

    @property
    def color(self) -> str | None:
        return self.__color

    @property
    def defense(self) -> int:
        return self.__defense

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


forest = Environment(on_color="green4", color="grey37",
                     symbol="\uF1BB", defense=1)
meadow = Environment(on_color="green3")
flower = Environment(on_color="green3", color="indian_red", symbol="*")
flower2 = Environment(on_color="green3", color="yellow", symbol="*")
flower3 = Environment(on_color="green3", color="cyan", symbol="*")
mountain = Environment(on_color="grey37", symbol="^")
water = Environment(on_color="blue", symbol="≈",
                    color="bright_blue", defense=-2)
