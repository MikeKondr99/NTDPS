import copy
import os
import keyboard  # type: ignore
from rich import print
from rich.panel import Panel
import random
import time
from typing import Tuple, Callable
from src.labs.lab2.environment import Environment, forest, flower, flower2, flower3, mountain, meadow, water
from perlin_noise import PerlinNoise  # type: ignore
Pos = Tuple[int, int]
Action = Callable[['GameFieldRenderer'], str]


class Field:

    def __init__(self, rows: int, cols: int, *, unit_cap: int = 30) -> None:
        self.__rows = rows
        self.__cols = cols
        self.players: list[str] = ["bright_red", "magenta"]
        self.playerid: int = 0
        self.__unit_cap = unit_cap
        self.__unit_count = 0
        self.environment: list[list[Environment]] = []
        self.units: list[list[Unit | None]] = []
        for i in range(0, self.rows):
            self.units.append([])
            for j in range(0, self.cols):
                self.units[i].append(None)
        self.generate()

    def current_player(self) -> str:
        return self.players[self.playerid]

    @property
    def rows(self) -> int:
        return self.__rows

    @property
    def cols(self) -> int:
        return self.__cols

    @property
    def unit_cap(self) -> int:
        return self.__unit_cap

    @property
    def unit_count(self) -> int:
        return self.__unit_count

    def add(self, unit: 'Unit', row: int, col: int) -> str:
        if self.unit_count >= self.unit_cap:
            return "Достигнут предел отрядов!"
        elif self.units[row][col] is not None:
            return "Клетка занята!"
        else:
            self.units[row][col] = unit
            return "success"

    def generate(self) -> None:
        p_river = PerlinNoise(0.5, random.randint(1, 1000))
        p_mountain = PerlinNoise(0.5, random.randint(1, 1000))
        p_forest = PerlinNoise(4, random.randint(1, 1000))
        p_flowers = PerlinNoise(7, random.randint(1, 1000))
        for i in range(0, self.rows):
            self.environment.append([])
            for j in range(0, self.cols):
                self.environment[i].append(meadow)
        for i in range(0, self.rows):
            for j in range(0, self.cols):
                # Леса
                val4 = p_flowers([i / self.rows, j / self.cols])
                if val4 > 0.14:
                    self.environment[i][j] = random.choice(
                        [flower, flower2, flower3]
                    )
                # Леса
                val3 = p_forest([i / self.rows, j / self.cols])
                if val3 > 0.14:
                    self.environment[i][j] = forest
                # Горы
                val2 = p_mountain([i / self.rows, j / self.cols])
                if val2 > 0.16 and val2 < 0.19:
                    self.environment[i][j] = mountain
                # Реки
                val = p_river([i / self.rows, j / self.cols])
                if val > 0.15 and val < 0.20:
                    self.environment[i][j] = water
        self.add(Base("bright_red"), 4, 4)
        self.add(Base("magenta"), 11, 11)


class Unit:

    def __init__(self, name: str, symbol: str, color: str, actions: dict[str, Action] = {}, /,
                 hp: int = 10,
                 max_hp: int = 10,
                 range: int = 0,
                 defense: int = 0
                 ):
        self.name = name
        self.color = color
        self.hp = hp
        self.max_hp = max_hp
        self.defense = 0
        self.symbol = symbol
        self.actions = actions
        self.range = 0

    def print(self) -> None:
        res = f"[{self.color}]{self.name}[/]\n" + \
            f"Health: {self.hp}/{self.max_hp}\n" + \
            f"Health: {self.defense}\n" + \
            f"Commands:\n"
        for kv in self.actions:
            res += f" ► {kv}"
        print(Panel.fit(res))


class GameFieldRenderer:
    def __init__(self, rows: int, cols: int) -> None:
        self.cursor: Tuple[int, int] = (5, 5)
        self.message: str = ""
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

    def print(self) -> None:
        os.system('cls')
        print(Panel.fit(
            f"""Player {1} stone {3} wood ...
Player {2} stone {4} wood ...
[{self.field.current_player()}]Move of Player {self.field.playerid + 1}[/]"""
        ))
        print(Panel.fit(self.__rich__()), end="")
        unit = self.field.units[self.cursor[0]][self.cursor[1]]
        if isinstance(unit, Unit):
            unit.print()
        print("log: ", self.message)

    def unit_at_cursor(self) -> None | Unit:
        return self.field.units[self.cursor[0]][self.cursor[1]]

    def unit_at_pos(self, pos: Pos) -> None | Unit:
        return self.field.units[pos[0]][pos[1]]

    def set_unit_at_pos(self, pos: Pos, unit: Unit | None) -> None:
        self.field.units[pos[0]][pos[1]] = unit

    def run(self) -> None:
        while True:
            if self.set_cursor():
                break
            self.message = ""
            self.print()
            unit = self.unit_at_cursor()
            if isinstance(unit, Unit) and unit.color == self.field.current_player():
                cmd = input("Choose command\n>>> ")
                if cmd in unit.actions:
                    res = (unit.actions[cmd])(self)
                    if res.startswith("!"):
                        self.message = f"[bright_red]{res[1:]}[/]"
                    else:
                        self.message = f"{res}"
                        self.field.playerid += 1
                        self.field.playerid %= len(self.field.players)

    def get_cursor(self) -> Pos:
        pos = self.cursor
        self.set_cursor()
        res = self.cursor
        self.cursor = pos
        return res

    def set_cursor(self) -> bool:
        self.cursor_visible = True
        time.sleep(0.1)
        self.print()
        while True:
            a = keyboard.is_pressed("a")
            w = keyboard.is_pressed("w")
            s = keyboard.is_pressed("s")
            d = keyboard.is_pressed("d")
            q = keyboard.is_pressed("q")
            enter = keyboard.is_pressed("enter")
            if q or a or w or s or d or enter:
                if q:
                    print("Ты вышел :(")
                    return True
                if a:
                    self.cursor = self.cursor[0], max(0, self.cursor[1] - 1)
                elif d:
                    self.cursor = self.cursor[0], min(
                        self.field.rows - 1, self.cursor[1] + 1)
                elif w:
                    self.cursor = max(0, self.cursor[0] - 1), self.cursor[1]
                elif s:
                    self.cursor = min(self.field.cols - 1,
                                      self.cursor[0] + 1), self.cursor[1]
                elif enter:
                    break
                self.print()
        input()
        self.cursor_visible = False
        self.print()
        return False


def distance(p1: Pos, p2: Pos) -> int:
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def skip() -> Action:
    def f(g: GameFieldRenderer) -> str:
        return ""
    return f


def spawn(unit: Callable[[], Unit]) -> Action:
    def f(g: GameFieldRenderer) -> str:
        pos = g.cursor
        g.message += "Choose adjacent cell\n"
        pos2 = g.get_cursor()
        if distance(pos, pos2) == 1 and not g.unit_at_pos(pos2):
            u = unit()
            g.field.add(u, pos2[0], pos2[1])
            return f"Unit {u.name} created"
        else:
            return "!Wrong cell input"
    return f


def build(unit: Callable[[], Unit]) -> Action:
    def f(g: GameFieldRenderer) -> str:
        pos = g.cursor
        g.message += "Choose adjacent cell\n"
        pos2 = g.get_cursor()
        if distance(pos, pos2) == 1 and not g.unit_at_pos(pos2):
            u = unit()
            g.field.add(u, pos2[0], pos2[1])
            g.set_unit_at_pos(pos, None)
            return f"Unit {u.name} created"
        else:
            return "!Wrong cell input"
    return f


def move(max: int) -> Action:

    def f(g: GameFieldRenderer) -> str:
        pos = g.cursor
        g.message += "Choose cell to move\n"
        pos2 = g.get_cursor()
        if distance(pos, pos2) <= max and not g.unit_at_pos(pos2):
            g.set_unit_at_pos(pos2, g.unit_at_pos(pos))
            g.set_unit_at_pos(pos, None)
            return f"Unit moved"
        else:
            return "! Wrong cell input"
    return f


def unlock(unkey: str, key: str, act: Action) -> Action:
    def f(g: GameFieldRenderer) -> str:
        me = g.unit_at_cursor()
        if me:
            me.actions.pop(unkey)
            me.actions[key] = act
        return f"{key} is available now"
    return f


def attack(dmg: int, range: int) -> Action:
    def f(g: GameFieldRenderer) -> str:
        pos = g.cursor
        g.message += "Choose cell to attack\n"
        pos2 = g.get_cursor()
        if distance(pos, pos2) <= range:
            unit = g.unit_at_pos(pos2)
            if unit:
                env_defense = g.field.environment[pos2[0]][pos2[1]].defense
                dmg2 = max(dmg - unit.defense - env_defense, 0)
                unit.hp -= dmg2
                if unit.hp <= 0:
                    g.set_unit_at_pos(pos2, None)
                    return f"Unit {unit.name} died"
                return f"Unit {unit.name} take {dmg2} damage"
            return "!Don't attack empty cell o_o"
        return "!To far"
    return f


def take_unit() -> Action:
    def f(g: GameFieldRenderer) -> str:
        pos = g.cursor
        owner = g.unit_at_pos(pos)
        g.message += "Choose adjacent to take\n"
        pos2 = g.get_cursor()
        if distance(pos, pos2) <= 1:
            unit = g.unit_at_pos(pos2)
            if unit and owner:
                if unit.color != owner.color:
                    return "Different color"
                owner.actions = unit.actions
                owner.actions.pop('move', None)
                owner.actions.pop('unpin', None)
                g.set_unit_at_pos(pos2, None)
                return f"Unit {unit.name} died"
            return "!Don't attack empty cell o_o"
        return "!To far"
    return f


def range_attack(dmg: int, range: int) -> Action:
    def f(g: GameFieldRenderer) -> str:
        pos = g.cursor
        owner = g.unit_at_cursor()
        if not owner:
            return "!unreachable"
        g.message += "Choose cell to attack\n"
        pos2 = g.get_cursor()
        if distance(pos, pos2) <= range + owner.range:
            unit = g.unit_at_pos(pos2)
            if unit:
                env_defense = g.field.environment[pos2[0]][pos2[1]].defense
                dmg2 = max(dmg - unit.defense - env_defense, 0)
                unit.hp -= dmg2
                if unit.hp <= 0:
                    g.set_unit_at_pos(pos2, None)
                    return f"Unit {unit.name} died"
                return f"Unit {unit.name} take {dmg2} damage"
            return "!Don't attack empty cell o_o"
        return "!To far"
    return f


def heal(heal: int, range: int) -> Action:
    def f(g: GameFieldRenderer) -> str:
        pos = g.cursor
        owner = g.unit_at_cursor()
        if not owner:
            return "!unreachable"
        g.message += "Choose cell to heal\n"
        pos2 = g.get_cursor()
        if distance(pos, pos2) <= range + owner.range:
            unit = g.unit_at_pos(pos2)
            if unit:
                unit.hp += heal
                unit.hp = min(unit.hp, unit.max_hp)
                return f"Unit {unit.name} healed {heal} damage"
            else:
                return "!Don't heal empty cell o_o"
        else:
            return "!To far"
    return f


def dash(max: int) -> Action:
    def f(g: GameFieldRenderer) -> str:
        pos = g.cursor
        g.message += "Choose cell to move\n"
        pos2 = g.get_cursor()
        if distance(pos, pos2) <= max and not g.unit_at_pos(pos2) and (pos[0] == pos2[0] or pos[1] == pos2[1]):
            g.set_unit_at_pos(pos2, g.unit_at_pos(pos))
            g.set_unit_at_pos(pos, None)
            return f"Unit moved"
        else:
            return "! Wrong cell input"
    return f


def pin(range: int) -> Action:
    def f(g: GameFieldRenderer) -> str:
        pos = g.cursor
        owner = g.unit_at_cursor()
        if not owner:
            return "!unreachable"
        g.message += "Choose cell to attack\n"
        pos2 = g.get_cursor()
        if distance(pos, pos2) <= range + owner.range:
            unit = g.unit_at_pos(pos2)
            if unit:
                if "move" in unit.actions:
                    mov = unit.actions.pop("move")
                    unit.actions["unpin"] = unlock("unpin", "move", mov)
                else:
                    return "! This unit cannot move"

                return f"Unit {unit.name} pinned"
            else:
                return "!Don't attack empty cell o_o"
        else:
            return "!To far"
    return f


def control(range: int, color: str) -> Action:
    def f(g: GameFieldRenderer) -> str:
        pos = g.cursor
        rang = range
        me = g.unit_at_cursor()
        g.message += "Choose unit to mind control\n"
        pos2 = g.get_cursor()
        if distance(pos, pos2) <= rang:
            unit = g.unit_at_pos(pos2)
            if unit and me:
                if "control" in unit.actions:
                    return "! Unit is already controlled"
                clor = unit.color
                if clor == 'black':
                    rang = 3
                me.actions.pop("control")
                unit.color, me.color = me.color, color
                unit.actions["control"] = control(min(rang, 1), clor)
                return f"Unit {unit.name} controlled"
            else:
                return "!Cell is empty"
        else:
            return "!To far"
    return f


class Warrior(Unit):

    def __init__(self, color: str) -> None:
        super().__init__("Warrior", "W", color, {
            "move": move(2),
            "attack": attack(6, 1),
            "dash": dash(3),
        },
        )
        self.defense = 1


class Healer(Unit):

    def __init__(self, color: str) -> None:
        super().__init__("Healer", "H", color, {
            "move": move(2),
            "heal": heal(2, 3),
        },
        )
        self.defense = 1
        self.range = 1


class Archer(Unit):

    def __init__(self, color: str) -> None:
        super().__init__("Archer", "A", color, {
            "move": move(2),
            "attack": attack(3, 3),
            "pin": pin(5),
        },
            hp=5,
            max_hp=5,
            range=2
        )


class Mage(Unit):

    def __init__(self, color: str) -> None:
        super().__init__("Mage", "M", color, {
            "move": move(2),
            "control": control(3, 'black'),
        },
            hp=5,
            max_hp=5
        )


class Militia(Unit):

    def __init__(self, color: str) -> None:
        super().__init__("Militia", "m", color, {
            "move": move(3),
            "attack": attack(2, 1)
        },
            hp=3,
            max_hp=5
        )


class Base(Unit):

    def __init__(self, color: str) -> None:
        super().__init__("Base", "▣", color, {
            "skip": skip(),
            "builder": spawn(lambda: Builder(color)),
            "militia": spawn(lambda: Militia(color))
        },
            max_hp=20,
            hp=20,
        )


class Barracks(Unit):

    def __init__(self, color: str) -> None:
        super().__init__("Barracks", "⌂", color, {
            "warrior": spawn(lambda: Warrior(color)),
            "archer": spawn(lambda: Archer(color)),
            "mage": spawn(lambda: Mage(color)),
            "healer": spawn(lambda: Healer(color))
        },
            max_hp=10,
            hp=10,
        )


class Builder(Unit):

    def __init__(self, color: str) -> None:
        super().__init__("Builder", "B", color, {
            "move": move(4),
            "barracks": build(lambda: Barracks(color)),
            "tower": build(lambda: Tower(color))
        },
            hp=1,
            max_hp=1,
        )


class Tower(Unit):

    def __init__(self, color: str) -> None:
        super().__init__("Tower", "T", color, {
            "take_unit": take_unit()
        },
            hp=20,
            max_hp=0,
            range=3
        )
