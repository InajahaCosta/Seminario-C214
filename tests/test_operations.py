import pytest
from calculator.operations import Calculator

@pytest.fixture
def numbers():
    return {
        "positive": (3, 2),
        "negative": (-1, 1),
        "zero": (3, 0),
        "float": (5.5, 2.5),
        "zero_division": (1, 0),
        "invalid_type_str": ("3", 2),
        "invalid_type_list": ([1, 2], 2),
    }

def test_add(numbers):
    assert Calculator.add(*numbers["positive"]) == 5
    assert Calculator.add(*numbers["negative"]) == 0
    with pytest.raises(TypeError):
        Calculator.add(*numbers["invalid_type_str"])
    with pytest.raises(TypeError):
        Calculator.add(*numbers["invalid_type_list"])

def test_subtract(numbers):
    assert Calculator.subtract(*numbers["positive"]) == 1
    assert Calculator.subtract(*numbers["negative"]) == -2
    with pytest.raises(TypeError):
        Calculator.subtract(*numbers["invalid_type_str"])
    with pytest.raises(TypeError):
        Calculator.subtract(*numbers["invalid_type_list"])

def test_multiply(numbers):
    assert Calculator.multiply(*numbers["positive"]) == 6
    assert Calculator.multiply(*numbers["zero"]) == 0
    with pytest.raises(TypeError):
        Calculator.multiply(*numbers["invalid_type_str"])
    with pytest.raises(TypeError):
        Calculator.multiply(*numbers["invalid_type_list"])

def test_divide(numbers):
    assert Calculator.divide(*numbers["positive"]) == 1.5
    assert Calculator.divide(*numbers["float"]) == 2.2
    with pytest.raises(ValueError):
        Calculator.divide(*numbers["zero_division"])
    with pytest.raises(TypeError):
        Calculator.divide(*numbers["invalid_type_str"])
    with pytest.raises(TypeError):
        Calculator.divide(*numbers["invalid_type_list"])
