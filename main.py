import os
from typing import Callable
import src.tasks.football as Task1  # Задача 1
import src.tasks.dictionary as Task2  # Задача 2
import src.labs.lab1.my_calc as calc  # Лабораторная 1.2
import subprocess  # для запуска питон ноутбуков


def run_notebook(path: str) -> None:
    print("Открываем интерактивную среду ...")
    subprocess.run(["nbopen", path])


def lab1_1() -> None:
    run_notebook("src/labs/lab1/ufo_data.ipynb")


def lab1_2() -> None:
    text = ""
    while text != "q":
        try:
            text = input("> ")
            print(calc.eval(text))
        except Exception as e:
            print(str(e))


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
        words: list[str] = [f.readline().rstrip("\n") for i in range(0, words_len)]
        inputs_len: int = int(f.readline())
        inputs: list[str] = [f.readline().rstrip("\n") for i in range(0, inputs_len)]
        d = Task2.WordDict()
        d.add_word(*words)
        errors: set[str] = set()
        for line in inputs:
            errors = errors.union(d.errors_in(line))
        print("\n".join(errors))


def task34() -> None:
    run_notebook("src/tasks/db.ipynb")


tasks: dict[str, Callable[[], None]] = {
    "t1": task1,
    "t2": task2,
    "t3": task34,
    "t4": task34,
    "l1.1": lab1_1,
    "l1.2": lab1_2,
}


def main() -> None:
    choice = ""
    while choice != "q":
        if not os.path.isdir("files"):
            os.mkdir("files")
        choice = input("Введите что запустить (t# или l#): ")
        if choice in tasks:
            if choice[0] == "t":
                print(f"ЗАДАЧА {choice[1:]}")
            elif choice[0] == "l":
                print(f"ЛАБОРАТОРНАЯ {choice[1:]}")
            tasks[choice]()
        else:
            hints = filter(lambda x: x.startswith(choice), tasks)
            if hints:
                print(f'Может вы имели ввиду {" ".join(hints)}')
            print(f"Не существует такого задания {choice}")
            input()


if __name__ == "__main__":
    main()
