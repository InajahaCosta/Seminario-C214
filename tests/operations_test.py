import pytest
from calculator.operations import Calculator

def test_add():
    assert Calculator.add(3, 2) == 5
    assert Calculator.add(-1, 1) == 0
    with pytest.raises(TypeError):
        Calculator.add("3", 2)
    with pytest.raises(TypeError):
        Calculator.add(3, "2")

def test_subtract():
    assert Calculator.subtract(3, 2) == 1
    assert Calculator.subtract(2, 3) == -1
    with pytest.raises(TypeError):
        Calculator.subtract("3", 2)
    with pytest.raises(TypeError):
        Calculator.subtract(3, "2")

def test_multiply():
    assert Calculator.multiply(3, 2) == 6
    assert Calculator.multiply(3, 0) == 0
    with pytest.raises(TypeError):
        Calculator.multiply("3", 2)
    with pytest.raises(TypeError):
        Calculator.multiply(3, "2")

def test_divide():
    assert Calculator.divide(6, 2) == 3
    assert Calculator.divide(5, 2) == 2.5
    with pytest.raises(ValueError):
        Calculator.divide(1, 0)
    with pytest.raises(TypeError):
        Calculator.divide("6", 2)
    with pytest.raises(TypeError):
        Calculator.divide(6, "2")