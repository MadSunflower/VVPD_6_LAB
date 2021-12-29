import pytest

from ..sequence import syracuse_sequence, syracuse_max


@pytest.fixture
def test_data():
    return 1


def test_loneliest_number(test_data):
    assert syracuse_sequence(test_data) == [1]


def test_one_max(test_data):
    assert syracuse_max(test_data) == 1


def test_big_number_max():
    assert syracuse_max(12345) == 41668


def test_zero_number():
    assert syracuse_sequence(0) == []


def test_default_number():
    assert syracuse_sequence(13) == [13, 40, 20, 10, 5, 16, 8, 4, 2, 1]