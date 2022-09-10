class WordDict:
    def __init__(self) -> None:
        self._words: set[str] = set()

    def add_word(self, *words: str) -> None:
        for word in words:
            self._words.add(word.lower())

    def check(self, word: str) -> bool:
        return word.lower() in self._words

    def errors_in(self, text: str, split: str = " ") -> set[str]:
        res: set[str] = set()
        for word in text.split(split):
            if word.lower() not in self._words and word != "":
                res.add(word.lower())
        return res
