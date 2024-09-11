# test_example.py

import pytest
from example import add, subtract

def test_add():
    assert add(2, 3) == 5  # This test should pass

def test_subtract():
    assert subtract(5, 3) == 2  # This test will fail
