
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
