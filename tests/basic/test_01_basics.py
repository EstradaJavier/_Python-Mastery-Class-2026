"""
Automated tests for 01_basics.py (Lesson 1).

This module implements a subset of the planned tests from
docs/specs/basic/01basicslessonsspec.md. It focuses on return‑value
behavior that is stable over time and easy for beginners to reason about.
"""

import importlib.util
from pathlib import Path
from datetime import date
import pytest


def _load_module(module_path: str):
    """Dynamically load the lesson module by file path."""
    path = Path(module_path)
    spec = importlib.util.spec_from_file_location("lesson_01_basics", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


# Path to the real lesson file in this repository.
LESSON_PATH = Path("lessons/01_basic_python_lessons/01_basics.py")


@pytest.mark.skipif(
    not LESSON_PATH.exists(),
    reason="Lesson file not found. Check LESSON_PATH in test_01_basics.py.",
)
def test_calculate_age_from_dob_returns_expected_years():
    """BASIC-01-Q-001: Age should be an integer in a valid range."""
    lesson = _load_module(str(LESSON_PATH))

    # Representative DOB case (edge behavior is covered in a future test)
    age = lesson.calculate_age_from_dob(date(2000, 1, 1))

    assert isinstance(age, int), "Age should be returned as an integer."
    assert age >= 0, "Age should not be negative for a valid birth date."


@pytest.mark.skipif(
    not LESSON_PATH.exists(),
    reason="Lesson file not found. Check LESSON_PATH in test_01_basics.py.",
)
def test_calculate_age_from_dob_handles_pre_birthday_case():
    """BASIC-01-Q-002: Birthday-not-yet-occurred should be handled correctly."""
    lesson = _load_module(str(LESSON_PATH))

    # Choose a DOB late in the year to exercise the pre-birthday logic.
    dob = date(2000, 12, 31)
    today = date.today()

    age = lesson.calculate_age_from_dob(dob)

    # Expected age based on the same logic as the lesson implementation.
    expected_age = today.year - dob.year - (
            (today.month, today.day) < (dob.month, dob.day)
    )

    assert age == expected_age, (
        "Age should correctly account for whether the birthday "
        "has occurred yet this year."
    )


@pytest.mark.skipif(
    not LESSON_PATH.exists(),
    reason="Lesson file not found. Check LESSON_PATH in test_01_basics.py.",
)
def test_create_profile_returns_documented_tuple_shape():
    """BASIC-01-Q-003: create_profile(False) returns a 10-item tuple."""
    lesson = _load_module(str(LESSON_PATH))

    profile = lesson.create_profile(False)

    assert isinstance(profile, tuple), "Profile should be returned as a tuple."
    assert len(profile) == 10, "Profile tuple should contain exactly 10 values."


@pytest.mark.skipif(
    not LESSON_PATH.exists(),
    reason="Lesson file not found. Check LESSON_PATH in test_01_basics.py.",
)
def test_create_profile_returns_expected_height_meters():
    """BASIC-01-Q-004: Height in meters should equal the documented value."""
    lesson = _load_module(str(LESSON_PATH))

    profile = lesson.create_profile(False)
    height_meters = profile[4]  # index per documented tuple order

    assert isinstance(height_meters, float), "Height in meters should be a float."
    assert height_meters == 1.78, (
        "Height in meters should be rounded to 1.78 for a 5'10\" profile."
    )


@pytest.mark.skipif(
    not LESSON_PATH.exists(),
    reason="Lesson file not found. Check LESSON_PATH in test_01_basics.py.",
)
@pytest.mark.parametrize(
    "age,height_meters,expected_retirement,expected_height_feet",
    [
        (63, 1.78, 2, 5.84),
        (40, 1.78, 25, 5.84),
    ],
)
def test_run_operations_returns_expected_values(
        age,
        height_meters,
        expected_retirement,
        expected_height_feet,
):
    """BASIC-01-Q-006: run_operations() returns correct numeric results."""
    lesson = _load_module(str(LESSON_PATH))

    years_to_retirement, height_feet_decimal = lesson.run_operations(
        age, height_meters
    )

    assert years_to_retirement == expected_retirement, (
        "Retirement calculation did not match the lesson formula."
    )
    assert height_feet_decimal == expected_height_feet, (
        "Height in decimal feet should match the rounded conversion."
    )