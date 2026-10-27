
import pytest
from calculate import calculate_total


def test_total_without_discount():
    assert calculate_total(200) == 210.00


def test_total_at_300():
    assert calculate_total(300) == 315.00


def test_total_above_300():
    assert calculate_total(400) == 378.00


def test_zero_amount():
    assert calculate_total(0) == 0.00


def test_negative_amount():
    with pytest.raises(ValueError):
        calculate_total(-100)
