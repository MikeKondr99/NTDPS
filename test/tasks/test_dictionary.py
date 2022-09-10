import pytest
from src.tasks.dictionary import WordDict


@pytest.fixture
def fix() -> WordDict:
    return WordDict()


def test_add_word(fix: WordDict) -> None:
    fix.add_word("word")
    assert fix.check("word") == True
    assert fix.check("WORD") == True
    assert fix.check("Word") == True
    assert fix.check("W0rd") == False


def test_add_multiple_word(fix: WordDict) -> None:
    fix.add_word("mango", "banana")
    assert fix.check("mango") == True
    assert fix.check("MaNgO") == True
    assert fix.check("banana") == True
    assert fix.check("BAnaNA") == True
    assert fix.check("word") == False
    assert fix.check("mango banana") == False
    assert fix.check("mango ") == False


def test_check_string(fix: WordDict) -> None:
    fix.add_word("we", "are", "Software", "genious")
    result = fix.errors_in("We Are The Software genous ")
    expected = {"genous", "the"}
    assert result == expected
