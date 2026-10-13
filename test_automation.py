
from triangle_classifier import classify_triangle
from decision_table import get_discount


# Lab 2: Triangle Classifier Tests

def test_equilateral_triangle():
    assert classify_triangle(5, 5, 5) == "Equilateral"


def test_isosceles_triangle():
    assert classify_triangle(5, 5, 3) == "Isosceles"


def test_scalene_triangle():
    assert classify_triangle(4, 5, 6) == "Scalene"


def test_invalid_triangle():
    assert classify_triangle(1, 2, 3) == "Invalid"


# Lab 4: Decision Table Tests

def test_premium_without_unpaid_bills():
    assert get_discount(True, False) == "Yes"


def test_premium_with_unpaid_bills():
    assert get_discount(True, True) == "No"


def test_nonpremium_without_unpaid_bills():
    assert get_discount(False, False) == "No"


def test_nonpremium_with_unpaid_bills():
    assert get_discount(False, True) == "No"
