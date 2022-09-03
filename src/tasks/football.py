'''
Задание 1
Тема: "Первичное ознакомление со средствами разработки".
Напишите программу, которая принимает на стандартный вход список игр футбольных команд 
с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.
За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
Формат ввода следующий:
В первой строке указано целое число n n n — количество завершенных игр.
После этого идет n n n строк, в которых записаны результаты игры в следующем формате:
Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой
Вывод программы необходимо оформить следующим образом:
Команда:Всего_игр Побед Ничьих Поражений Всего_очков
Порядок вывода команд произвольный.

Sample Input:
3
Спартак;9;Зенит;10
Локомотив;12;Зенит;3
Спартак;8;Локомотив;15

Sample Output:
Спартак:2 0 0 2 0
Зенит:2 1 0 1 3
Локомотив:2 2 0 0 6 

'''

from typing import Tuple, cast

def main() -> None:
    gd = GamesData()
    gd.add_data_str('Спартак;9;Зенит;10')
    gd.add_data_str('Локомотив;12;Зенит;3')
    gd.add_data_str('Спартак;8;Локомотив;15')

class GamesData:

    def  __init__(self) -> None:
        self.data:dict[str,Tuple[int,int,int,int,int]] = {} # team: (all,win,tie,los,scr)

    def add_data(self,team1:str, score1: int, team2: str, score2: int) -> bool:
        if team1 not in self.data:
            self.data[team1] = (0,0,0,0,0)
        if team2 not in self.data:
            self.data[team2] = (0,0,0,0,0)
        if score1 > score2: # win
            self._add_win(team1)
            self._add_lose(team2)
        elif score2 > score1: #lose
            self._add_lose(team1)
            self._add_win(team2)
        else:
            self.add_tie(team1)
            self.add_tie(team2)
        return True

    def _add_win(self,team:str) -> None:
        self.data[team] = cast(Tuple[int,int,int,int,int],tuple(map(lambda x, y: x + y, self.data[team] , (1,1,0,0,3))))

    def _add_lose(self,team:str) -> None:
        self.data[team] = cast(Tuple[int,int,int,int,int],tuple(map(lambda x, y: x + y, self.data[team] , (1,0,0,1,0))))

    def add_tie(self,team:str) -> None:
        self.data[team] = cast(Tuple[int,int,int,int,int],tuple(map(lambda x, y: x + y, self.data[team] , (1,0,1,0,1))))

    # data in format "team1;score;team2;score"
    def add_data_str(self,data: str) -> bool:
        list = data.split(';')
        if len(list)!=4:
            return False
        return self.add_data(list[0],int(list[1]),list[2],int(list[3]))

    def get_info(self,team: str) -> str | None: # all win tie los score
        if team in self.data:
            return " ".join(map(str,self.data[team]))
        else:
            return None

    def get_all_info(self) -> str: # team: all win tie los score ...
        res = ""
        for key in sorted(self.data.items()):
            res += f"{key[0]}: {self.get_info(key[0])}\n"
        return res.rstrip('\n')


if __name__ == '__main__':
    main()