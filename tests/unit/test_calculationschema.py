import pytest
from pydantic import ValidationError
from app.schemas.calculation import CalculationCreate

@pytest.mark.parametrize(
    "a, b, operation",
    [
        (10, 5, "add"),
        (10, 5, "subtract"),
        (10, 5, "multiply"),
        (10, 5, "divide"),
    ],
)
def test_valid_calculation_schema(a, b, operation):
    calculation = CalculationCreate(a=a, b=b, type=operation)

    assert calculation.a == a
    assert calculation.b == b
    assert calculation.type == operation

def test_invalid_calculation_operation():
    with pytest.raises(ValidationError):
        CalculationCreate(a=10, b=5, type="power")

def test_calculation_divide_by_zero():
    with pytest.raises(ValidationError, match="Cannot divide by zero"):
        CalculationCreate(a=10, b=0, type="divide")

def test_calculation_missing_required_field():
    with pytest.raises(ValidationError):
        CalculationCreate(a=10, type="add")