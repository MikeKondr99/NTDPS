
from cmath import exp
import unittest
from src.tasks.dictionary import WordDict

class TestWordDict(unittest.TestCase):

    def test_add_word(self) -> None:
        d = WordDict()
        d.add_word('word')
        self.assertEqual(d.check('word'),True)
        self.assertEqual(d.check('WORD'),True)
        self.assertEqual(d.check('Word'),True)
        self.assertEqual(d.check('W0rd'),False)

    def test_add_multiple_word(self) -> None:
        d = WordDict()
        d.add_word('mango','banana')
        self.assertEqual(d.check('mango'),True)
        self.assertEqual(d.check('MaNgO'),True)
        self.assertEqual(d.check('banana'),True)
        self.assertEqual(d.check('BAnaNA'),True)
        self.assertEqual(d.check('word'),False)
        self.assertEqual(d.check('mango banana'),False)
        self.assertEqual(d.check('mango '),False)

    def test_check_string(self) -> None:
        d = WordDict()
        d.add_word('we','are','Software','genious')
        result = d.errors_in("We Are The Software genous ")
        expected = {"genous","the"}
        self.assertEqual(result,expected)

if __name__ == '__main__':
    unittest.main()