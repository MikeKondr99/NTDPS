
from src.tasks.football import GamesData

def task1() -> None:
    path = input("Путь к файлу данных: ")
    with open(path) as f:
        lines = f.readlines()
        data = GamesData()
        for line in lines:
            if not data.add_data_str(line):
                print("Строчка " + line + " не корректна")
        print(data.get_all_info())

def main() -> None:
    choice = input("Введите что запустить (t# или l#): ")
    if choice == "t1":
        task1()
    else:
        print(f"Не существует такого задания {choice}")

if __name__ == "__main__":
    main()
