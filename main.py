import os
from rich import print
from typing import Callable
import src.tasks.football as Task1  # Задача 1
import src.tasks.dictionary as Task2  # Задача 2
import src.labs.lab1.my_calc as calc  # Лабораторная 1.2
from src.labs.lab2.cui import GameFieldRenderer
import subprocess  # для запуска питон ноутбуков


def run_notebook(path: str) -> None:
    print("Открываем интерактивную среду : D ...")
    subprocess.run(["nbopen", path])


def lab1() -> None:
    print("Лабораторная 1")
    text = ""
    while text != "q":
        try:
            text = input("> ")
            print(calc.eval(text))
        except Exception as e:
            print(str(e))
    return
    print("Открываем интерактивную среду : D ...")
    subprocess.run(["nbopen", "src/labs/lab1/ufo_data.ipynb"])


def task1() -> None:
    path = input("Путь к файлу данных: ")
    with open(path) as f:
        lines = f.readlines()
        data = Task1.GamesData()
        for line in lines:
            if not data.add_data_str(line):
                print(f'Строка "{line}" не корректна')
        print(data.get_all_info())


def task2() -> None:
    path = input("Путь к файлу: ")

    with open(path) as f:
        words_len: int = int(f.readline())
        words: list[str] = [f.readline().rstrip("\n")
                            for i in range(0, words_len)]
        inputs_len: int = int(f.readline())
        inputs: list[str] = [f.readline().rstrip("\n")
                             for i in range(0, inputs_len)]
        d = Task2.WordDict()
        d.add_word(*words)
        errors: set[str] = set()
        for line in inputs:
            errors = errors.union(d.errors_in(line))
        print("\n".join(errors))


def task34() -> None:
    run_notebook("src/tasks/db.ipynb")


def task4() -> None:
    run_notebook("src/tasks/db.ipynb")


all_colors = [
    "black",
    "red",
    "green",
    "yellow",
    "blue",
    "magenta",
    "cyan",
    "white",
    "bright_black",
    "bright_red",
    "bright_green",
    "bright_yellow",
    "bright_blue",
    "bright_magenta",
    "bright_cyan",
    "bright_white",
    "grey0",
    "navy_blue",
    "dark_blue",
    "blue3",
    "blue1",
    "dark_green",
    "deep_sky_blue4",
    "dodger_blue3",
    "dodger_blue2",
    "green4",
    "spring_green4",
    "turquoise4",
    "deep_sky_blue3",
    "dodger_blue1",
    "dark_cyan",
    "light_sea_green",
    "deep_sky_blue2",
    "deep_sky_blue1",
    "green3",
    "spring_green3",
    "cyan3",
    "dark_turquoise",
    "turquoise2",
    "green1",
    "spring_green2",
    "spring_green1",
    "medium_spring_green",
    "cyan2",
    "cyan1",
    "purple4",
    "purple3",
    "blue_violet",
    "grey37",
    "medium_purple4",
    "slate_blue3",
    "royal_blue1",
    "chartreuse4",
    "pale_turquoise4",
    "steel_blue",
    "steel_blue3",
    "cornflower_blue",
    "dark_sea_green4",
    "cadet_blue",
    "sky_blue3",
    "chartreuse3",
    "sea_green3",
    "aquamarine3",
    "medium_turquoise",
    "steel_blue1",
    "sea_green2",
    "sea_green1",
    "dark_slate_gray2",
    "dark_red",
    "dark_magenta",
    "orange4",
    "light_pink4",
    "plum4",
    "medium_purple3",
    "slate_blue1",
    "wheat4",
    "grey53",
    "light_slate_grey",
    "medium_purple",
    "light_slate_blue",
    "yellow4",
    "dark_sea_green",
    "light_sky_blue3",
    "sky_blue2",
    "chartreuse2",
    "pale_green3",
    "dark_slate_gray3",
    "sky_blue1",
    "chartreuse1",
    "light_green",
    "aquamarine1",
    "dark_slate_gray1",
    "deep_pink4",
    "medium_violet_red",
    "dark_violet",
    "purple",
    "medium_orchid3",
    "medium_orchid",
    "dark_goldenrod",
    "rosy_brown",
    "grey63",
    "medium_purple2",
    "medium_purple1",
    "dark_khaki",
    "navajo_white3",
    "grey69",
    "light_steel_blue3",
    "light_steel_blue",
    "dark_olive_green3",
    "dark_sea_green3",
    "light_cyan3",
    "light_sky_blue1",
    "green_yellow",
    "dark_olive_green2",
    "pale_green1",
    "dark_sea_green2",
    "pale_turquoise1",
    "red3",
    "deep_pink3",
    "magenta3",
    "dark_orange3",
    "indian_red",
    "hot_pink3",
    "hot_pink2",
    "orchid",
    "orange3",
    "light_salmon3",
    "light_pink3",
    "pink3",
    "plum3",
    "violet",
    "gold3",
    "light_goldenrod3",
    "tan",
    "misty_rose3",
    "thistle3",
    "plum2",
    "yellow3",
    "khaki3",
    "light_yellow3",
    "grey84",
    "light_steel_blue1",
    "yellow2",
    "dark_olive_green1",
    "dark_sea_green1",
    "honeydew2",
    "light_cyan1",
    "red1",
    "deep_pink2",
    "deep_pink1",
    "magenta2",
    "magenta1",
    "orange_red1",
    "indian_red1",
    "hot_pink",
    "medium_orchid1",
    "dark_orange",
    "salmon1",
    "light_coral",
    "pale_violet_red1",
    "orchid2",
    "orchid1",
    "orange1",
    "sandy_brown",
    "light_salmon1",
    "light_pink1",
    "pink1",
    "plum1",
    "gold1",
    "light_goldenrod2",
    "navajo_white1",
    "misty_rose1",
    "thistle1",
    "yellow1",
    "light_goldenrod1",
    "khaki1",
    "wheat1",
    "cornsilk1",
    "grey100",
    "grey3",
    "grey7",
    "grey11",
    "grey15",
    "grey19",
    "grey23",
    "grey27",
    "grey30",
    "grey35",
    "grey39",
    "grey42",
    "grey46",
    "grey50",
    "grey54",
    "grey58",
    "grey62",
    "grey66",
    "grey70",
    "grey74",
    "grey78",
    "grey82",
    "grey85",
    "grey89",
    "grey93",
]


def lab4() -> None:
    run_notebook("src/labs/lab4/lab4.ipynb")


def lab2() -> None:
    """for color in all_colors:
        print(f"[{color}]{color}[/]")
    input()"""
    game = GameFieldRenderer(16, 16)
    game.run()


tasks: dict[str, Callable[[], None]] = {
    "t1": task1,
    "t2": task2,
    "t3": task34,
    "t4": task34,
    "l1": lab1,
    "l2": lab2,
}


def main() -> None:
    print("[green on blue]Fear is the mind-killer[/]")
    if not os.path.isdir("files"):
        os.mkdir("files")
    choice = input("Введите что запустить (t# или l#): ")
    if choice in tasks:
        if choice[0] == "t":
            print("[blue]Задача", choice[1:])
        else:
            print("[blue]Задача", choice[1:])
        tasks[choice]()
    else:
        print(f"[red]Не существует такого задания {choice}")


if __name__ == "__main__":
    main()
