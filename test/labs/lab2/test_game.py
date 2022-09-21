import pytest
from src.labs.lab2.game import Field, Environment, Unit


def test_field_creation() -> None:
    field = Field(30, 15)
    assert field.cols == 30
    assert field.rows == 30


def test_field_add_unit() -> None:
    field = Field(30, 15)
    field.add(Unit("$", "black"), 3, 3)
