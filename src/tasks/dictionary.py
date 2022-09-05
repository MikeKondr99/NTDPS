
import pstats


class WordDict:

    def __init__(self) -> None:
        self._words:set[str] = set()


    def add_word(self,*words:str) -> None:
        for word in words:
            self._words.add(word.lower())

    def check(self,word: str,split:str | None = None) -> bool:
        if(split == None):
            return word.lower() in self._words
        else:
            raise NotImplementedError


    pass