# tests/test_fizzbuzz.py
# Unit tests for the fizzbuzz_result() function
# Uses pytest — run with the green play button or the terminal

import sys
import os

# This line helps Python find your lessons folder
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lessons', 'additional_lessons'))

from fizzbuzz import fizzbuzz_result


# ─────────────────────────────────────────────
# SCENARIO GROUP 1: FizzBuzz (divisible by both 3 AND 5)
# ─────────────────────────────────────────────

def test_fizzbuzz_at_15():
    """15 is divisible by both 3 and 5 → should return 'FizzBuzz'"""
    assert fizzbuzz_result(15) == "FizzBuzz"

def test_fizzbuzz_at_30():
    """30 is divisible by both 3 and 5 → should return 'FizzBuzz'"""
    assert fizzbuzz_result(30) == "FizzBuzz"

def test_fizzbuzz_at_45():
    """45 is divisible by both 3 and 5 → should return 'FizzBuzz'"""
    assert fizzbuzz_result(45) == "FizzBuzz"


# ─────────────────────────────────────────────
# SCENARIO GROUP 2: Fizz (divisible by 3, NOT 5)
# ─────────────────────────────────────────────

def test_fizz_at_3():
    """3 is divisible by 3 → should return 'Fizz'"""
    assert fizzbuzz_result(3) == "Fizz"

def test_fizz_at_6():
    """6 is divisible by 3 → should return 'Fizz'"""
    assert fizzbuzz_result(6) == "Fizz"

def test_fizz_at_9():
    """9 is divisible by 3 → should return 'Fizz'"""
    assert fizzbuzz_result(9) == "Fizz"


# ─────────────────────────────────────────────
# SCENARIO GROUP 3: Buzz (divisible by 5, NOT 3)
# ─────────────────────────────────────────────

def test_buzz_at_5():
    """5 is divisible by 5 → should return 'Buzz'"""
    assert fizzbuzz_result(5) == "Buzz"

def test_buzz_at_10():
    """10 is divisible by 5 → should return 'Buzz'"""
    assert fizzbuzz_result(10) == "Buzz"

def test_buzz_at_25():
    """25 is divisible by 5 → should return 'Buzz'"""
    assert fizzbuzz_result(25) == "Buzz"


# ─────────────────────────────────────────────
# SCENARIO GROUP 4: Regular numbers (no Fizz or Buzz)
# ─────────────────────────────────────────────

def test_regular_number_1():
    """1 is not divisible by 3 or 5 → should return '1' as a string"""
    assert fizzbuzz_result(1) == "1"

def test_regular_number_7():
    """7 is not divisible by 3 or 5 → should return '7' as a string"""
    assert fizzbuzz_result(7) == "7"

def test_regular_number_11():
    """11 is not divisible by 3 or 5 → should return '11' as a string"""
    assert fizzbuzz_result(11) == "11"


# ─────────────────────────────────────────────
# SCENARIO GROUP 5: Edge Cases
# ─────────────────────────────────────────────

def test_edge_case_number_1():
    """The minimum valid input (1) should return '1'"""
    assert fizzbuzz_result(1) == "1"

def test_edge_case_100():
    """100 is divisible by 5 but NOT 3 → should return 'Buzz'"""
    assert fizzbuzz_result(100) == "Buzz"

def test_return_type_is_always_string():
    """fizzbuzz_result should always return a string, never an int"""
    result = fizzbuzz_result(7)
    assert isinstance(result, str), f"Expected str, got {type(result)}"
