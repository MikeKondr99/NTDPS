import pytest
from src.tasks.dictionary import WordDict


@pytest.fixture
def fix() -> WordDict:
    return WordDict()


def test_add_word(fix: WordDict) -> None:
    fix.add_word("word")
    assert fix.check("word")
    assert fix.check("WORD")
    assert fix.check("Word")
    assert not fix.check("W0rd")


def test_add_multiple_word(fix: WordDict) -> None:
    fix.add_word("mango", "banana")
    assert fix.check("mango")
    assert fix.check("MaNgO")
    assert fix.check("banana")
    assert fix.check("BAnaNA")
    assert not fix.check("word")
    assert not fix.check("mango banana")
    assert not fix.check("mango ")


def test_check_string(fix: WordDict) -> None:
    fix.add_word("we", "are", "Software", "genious")
    result = fix.errors_in("We Are The Software genous ")
    expected = {"genous", "the"}
    assert result == expected
