import pytest
from app.operations.calculationfactory import calculate

@pytest.mark.parametrize(
    "a, b, operation, expected",
    [
        (10, 5, "add", 15),
        (10, 5, "subtract", 5),
        (10, 5, "multiply", 50),
        (10, 5, "divide", 2.0),
    ],
)
def test_calculate(a, b, operation, expected):
    assert calculate(a, b, operation) == expected

def test_calculate_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero!"):
        calculate(10, 0, "divide")

def test_calculate_unsupported_operation():
    with pytest.raises(ValueError, match="Unsupported operation: power"):
        calculate(10, 5, "power")