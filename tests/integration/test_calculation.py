import uuid
import pytest
from sqlalchemy.exc import IntegrityError

from app.models.user import User
from app.models.calculation import Calculation

def test_create_calculation(db_session):
    # Create a user first
    user = User(
        first_name="Test",
        last_name="User",
        email="calculation_test@example.com",
        username="calculationtest",
        password="password123"
    )

    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)

    # Create a calculation associated with that user
    calculation = Calculation(
        a=10,
        b=5,
        type="add",
        result=15,
        user_id=user.id
    )

    db_session.add(calculation)
    db_session.commit()
    db_session.refresh(calculation)

    # Verify the calculation was saved
    saved_calculation = db_session.query(Calculation).filter_by(
        id=calculation.id
    ).first()

    assert saved_calculation is not None
    assert saved_calculation.a == 10
    assert saved_calculation.b == 5
    assert saved_calculation.type == "add"
    assert saved_calculation.result == 15
    assert saved_calculation.user_id == user.id

def test_calculation_user_relationship(db_session):
    user = User(
        first_name="Relationship",
        last_name="Test",
        email="relationship_test@example.com",
        username="relationshiptest",
        password="password123"
    )

    calculation = Calculation(
        a=20,
        b=4,
        type="divide",
        result=5,
        user=user
    )

    db_session.add(user)
    db_session.add(calculation)
    db_session.commit()
    db_session.refresh(user)
    db_session.refresh(calculation)

    # Verify the relationship from User to Calculation
    assert calculation in user.calculations

    # Verify the relationship from Calculation to User
    assert calculation.user.id == user.id

def test_calculation_invalid_user(db_session):
    invalid_user_id = uuid.uuid4()

    calculation = Calculation(
        a=10,
        b=5,
        type="add",
        result=15,
        user_id=invalid_user_id
    )

    db_session.add(calculation)

    with pytest.raises(IntegrityError):
        db_session.commit()

    db_session.rollback()