from app import operations
import pytest

# ADD
def test_add():
    assert operations.add(2, 3) == 5
    assert operations.add(2.5, 3) == 5.5

# SUBTRACT
def test_subtract():
    assert operations.subtract(5, 3) == 2
    assert operations.subtract(5.5, 2) == 3.5

# MULTIPLY
def test_multiply():
    assert operations.multiply(2, 3) == 6
    assert operations.multiply(2.5, 4) == 10.0

# DIVIDE
def test_divide():
    assert operations.divide(6, 3) == 2.0
    assert operations.divide(5.5, 2) == 2.75

# DIVIDE BY ZERO
def test_divide_by_zero():
    with pytest.raises(ValueError):
        operations.divide(5, 0)