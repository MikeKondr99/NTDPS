import pytest
from src.tasks.football import GamesData


@pytest.fixture
def fix() -> GamesData:
    return GamesData()


def test_lose_match(fix: GamesData) -> None:
    fix.add_data("Спартак", 4, "Зенит", 6)
    assert fix.get_info("Спартак") == "1 0 0 1 0"
    assert fix.get_info("Зенит") == "1 1 0 0 3"


def test_win_match(fix: GamesData) -> None:
    fix.add_data("Спартак", 7, "Зенит", 6)
    assert fix.get_info("Спартак") == "1 1 0 0 3"
    assert fix.get_info("Зенит") == "1 0 0 1 0"


def test_tie_match(fix: GamesData) -> None:
    fix.add_data("Спартак", 6, "Зенит", 6)
    assert fix.get_info("Спартак") == "1 0 1 0 1"
    assert fix.get_info("Зенит") == "1 0 1 0 1"


def test_accumulative_win(fix: GamesData) -> None:
    fix.add_data("Спартак", 7, "Зенит", 6)
    fix.add_data("Спартак", 13, "", 2)
    assert fix.get_info("Спартак") == "2 2 0 0 6"


def test_no_info(fix: GamesData) -> None:
    assert fix.get_info("Спартак") == None


def test_example(fix: GamesData) -> None:
    fix.add_data_str("Спартак;9;Зенит;10")
    fix.add_data_str("Локомотив;12;Зенит;3")
    fix.add_data_str("Спартак;8;Локомотив;15")
    assert fix.get_info("Спартак") == "2 0 0 2 0"
    assert fix.get_info("Зенит") == "2 1 0 1 3"
    assert fix.get_info("Локомотив") == "2 2 0 0 6"
    assert fix.get_info("Челси") == None


def test_all_info(fix: GamesData) -> None:
    fix.add_data_str("Спартак;9;Зенит;10")
    fix.add_data_str("Локомотив;12;Зенит;3")
    fix.add_data_str("Спартак;8;Локомотив;15")
    result = set(fix.get_all_info().split("\n"))
    expected = {"Зенит: 2 1 0 1 3", "Локомотив: 2 2 0 0 6", "Спартак: 2 0 0 2 0"}
    expected2 = {"Локомотив: 2 2 0 0 6", "Зенит: 2 1 0 1 3", "Спартак: 2 0 0 2 0"}
    assert result == expected
    assert result == expected2
