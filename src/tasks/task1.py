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

def main() -> None:
    gd = GamesData()
    gd.adddatastr('Спартак;9;Зенит;10')
    gd.adddatastr('Локомотив;12;Зенит;3')
    gd.adddatastr('Спартак;8;Локомотив;15')

class GamesData:

    def  __init__(self) -> None:
        self.data:dict = {} # team: (all,win,tie,los,scr)

    def adddata(self,team1:str, score1: int, team2: str, score2: int) -> bool:
        if(team1 not in self.data):
            self.data[team1] = (0,0,0,0,0)
        if(team2 not in self.data):
            self.data[team2] = (0,0,0,0,0)
        if score1 > score2: # win
            self.__addWin(team1)
            self.__addLose(team2)
        elif score2 > score1: #lose
            self.__addLose(team1)
            self.__addWin(team2)
        else:
            self.__addTie(team1)
            self.__addTie(team2)
        return True

    def __addWin(self,team:str) -> None:
        self.data[team] = tuple(map(lambda x, y: x + y, self.data[team] , (1,1,0,0,3)))

    def __addLose(self,team:str) -> None:
        self.data[team] = tuple(map(lambda x, y: x + y, self.data[team] , (1,0,0,1,0)))

    def __addTie(self,team:str) -> None:
        self.data[team] = tuple(map(lambda x, y: x + y, self.data[team] , (1,0,1,0,1)))

    # data in format "team1;score;team2;score"
    def adddatastr(self,data: str) -> bool:
        list = data.split(';')
        if len(list)!=4:
            return False
        return self.adddata(list[0],int(list[1]),list[2],int(list[3]))

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