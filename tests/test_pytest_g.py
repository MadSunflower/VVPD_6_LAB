import pytest

from ..sequence import syracuse_sequence, syracuse_max


@pytest.fixture
def test_data():
    return 1


def test_loneliest_number(test_data):
    """
    Test for fixture, testing 1 for sequence
    :param test_data: data from fixture
    :return: sequence for 1
    """
    assert syracuse_sequence(test_data) == [1]


def test_one_max(test_data):
    """
    Test for fixture, testing 1 for maximum
    :param test_data: data from fixture
    :return: maximum from sequence of 1
    """
    assert syracuse_max(test_data) == 1


def test_big_number_max():
    """
    Test for big number, testing 12345 for maximum
    :return: maximum from sequence of 12345
    """
    assert syracuse_max(12345) == 41668


def test_zero_number():
    """
    Test for sequence from zero
    :return: sequence for 0
    """
    assert syracuse_sequence(0) == []


def test_default_number():
    """
    Test for "normal" number sequence, testing from 13
    :return: sequence for 13
    """
    assert syracuse_sequence(13) == [13, 40, 20, 10, 5, 16, 8, 4, 2, 1]


@pytest.mark.parametrize('t_input,t_expect', [(5, 16), (13, 40), (0, 0)])
def test_default_max(t_input, t_expect):
    """
    Parameter test, testing 5, 13 and 0 for maximum
    :param t_input: Data from parametrize, input for max function
    :param t_expect: Data from parametrize, input result of max function
    :return: maximum from sequence of 5, 13 and 0
    """
    assert syracuse_max(t_input) == t_expect