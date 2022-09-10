import os
from typing import Callable
import src.tasks.football as Task1  # Задача 1
import src.tasks.dictionary as Task2  # Задача 2
import src.tasks.db1 as Task34  # Задача 3 и 4
import src.labs.lab1.my_calc as calc  # Лабораторная 1.2
import subprocess  # для запуска питон ноутбуков


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
    subprocess.run(["nbopen", "src/labs/ufo_data.ipynb"])


def task1() -> None:
    print("ЗАДАЧА 1")
    path = input("Путь к файлу данных: ")
    with open(path) as f:
        lines = f.readlines()
        data = Task1.GamesData()
        for line in lines:
            if not data.add_data_str(line):
                print(f'Строка "{line}" не корректна')
        print(data.get_all_info())


def task2() -> None:
    print("ЗАДАЧА 2")
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


def task3() -> None:
    print("ЗАДАЧА 3")
    Task34.create("files/database.sqlite")


def task4() -> None:
    print("ЗАДАЧА 4")
    Task34.create("files/database.sqlite", True)


tasks: dict[str, Callable[[], None]] = {
    "t1": task1,
    "t2": task2,
    "t3": task3,
    "t4": task4,
    "l1": lab1,
}


def main() -> None:
    if not os.path.isdir("files"):
        os.mkdir("files")
    choice = input("Введите что запустить (t# или l#): ")
    if choice in tasks:
        tasks[choice]()
    else:
        print(f"Не существует такого задания {choice}")


if __name__ == "__main__":
    main()
