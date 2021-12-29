import unittest

from ..sequence import syracuse_sequence, syracuse_max


class TestFiveMax(unittest.TestCase):
    """
    Testing five to max
    """

    def setUp(self) -> None:
        self.test_data = 5

    def test_sequence_max(self):
        self.assertEqual(syracuse_max(self.test_data), 16)


class TestFiveSequence(unittest.TestCase):
    """
    Testing five to sequence
    """

    def setUp(self) -> None:
        self.test_data = 5

    def test_sequence(self):
        self.assertEqual(syracuse_sequence(self.test_data), [5, 16, 8, 4, 2, 1])


class TestNineMax(unittest.TestCase):
    """
    Testing nine to max
    """

    def setUp(self) -> None:
        self.test_data = 9

    def test_sequence_max(self):
        self.assertEqual(syracuse_max(self.test_data), 52)


class TestNineSequence(unittest.TestCase):
    """
    Testing nine to sequence
    """

    def setUp(self) -> None:
        self.test_data = 9

    def test_sequence(self):
        self.assertEqual(syracuse_sequence(self.test_data),
                         [9, 28, 14, 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1])


class ParametrizedTest(unittest.TestCase):
    """
    Parametrized test to 0, 5,
    """

    def setUp(self) -> None:
        self.test_data = [(0, 0), (5, 16), (9, 52)]

    def test_param_max(self):
        for one_data in self.test_data:
            with self.subTest(one_data=one_data):
                self.assertEqual(syracuse_max(one_data[0]), one_data[1])
