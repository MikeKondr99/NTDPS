import os
from src.labs.lab3.window import run as lab3
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


def lab2() -> None:
    game = GameFieldRenderer(10, 10)
    game.run()


tasks: dict[str, Callable[[], None]] = {
    "t1": task1,
    "t2": task2,
    "t3": task34,
    "t4": task34,
    "l1": lab1,
    "l2": lab2,
    "l3": lab3,
}


def main() -> None:
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
