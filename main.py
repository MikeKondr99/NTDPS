
from typing import Callable
from src.tasks.football import GamesData
from src.tasks.dictionary import WordDict

def task1() -> None:
    path = input("Путь к файлу данных: ")
    with open(path) as f:
        lines = f.readlines()
        data = GamesData()
        for line in lines:
            if not data.add_data_str(line):
                print("Строчка " + line + " не корректна")
        print(data.get_all_info())

def task2() -> None:
    path = input("Путь к файлу: ")

    with open(path) as f:
        words_len:int = int(f.readline())
        words:list[str] = [f.readline().rstrip('\n') for i in range(0,words_len)]
        inputs_len:int = int(f.readline())
        inputs:list[str] = [f.readline().rstrip('\n') for i in range(0,inputs_len)]
        d = WordDict()
        d.add_word(*words)
        errors:set[str] = set()
        for line in inputs:
            errors = errors.union(d.errors_in(line))
        print("\n".join(errors))



tasks:dict[str,Callable[[],None]] = {
    "t1":task1,
    "t2":task2,
}
            

def main() -> None:
    choice = input("Введите что запустить (t# или l#): ")
    if(choice in tasks):
        tasks[choice]()
    else:
        print(f"Не существует такого задания {choice}")

if __name__ == "__main__":
    main()
