import pytest
from src.labs.lab2 import Field, Environment, Unit


success = "success"


def test_field_creation() -> None:
    field = Field(30, 15)
    assert field.cols == 15
    assert field.rows == 30
    assert field.unit_cap == 30
    assert field.unit_count == 0


def test_field_add_unit() -> None:
    field = Field(30, 15)
    result = field.add(Unit("$", "black"), 3, 3)
    assert field.cols == 15
    assert field.rows == 30
    assert field.unit_cap == 30
    assert field.unit_count == 1
    assert result == success
