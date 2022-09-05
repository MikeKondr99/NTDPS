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
        for key in self.data:
            res += f'{key}: {self.get_info(key)}\n'
        return res.rstrip('\n')


if __name__ == '__main__':
    main()