'''
Простейшая система проверки орфографии может быть основана на использовании списка известных слов.
Если введённое слово не найдено в этом списке, оно помечается как "ошибка".
Формат ввода следующий:
На вход программе первой строкой передаётся количество d известных нам слов, после чего на d строках указываются эти слова.
Затем передаётся количество l строк текста для проверки, после чего l строк текста.
Выведите уникальные "ошибки" в произвольном порядке. Работу производите без учёта регистра.
Sample Input:

5
champions
we
are
Software
genious
3
We are the Software genious
We Are The Software genous
Softwqare

Sample Output:

genous
champignons
the
softwqare
'''

class WordDict:

    def __init__(self) -> None:
        self._words:set[str] = set()


    def add_word(self,*words:str) -> None:
        for word in words:
            self._words.add(word.lower())

    def check(self,word: str) -> bool:
        return word.lower() in self._words

    def errors_in(self,text: str,split:str =' ') -> set[str]:
        res:set[str] = set()
        for word in text.split(split):
            if word.lower() not in self._words and word != '':
                res.add(word.lower())
        return res




        
    

