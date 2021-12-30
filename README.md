# Лабораторная работа №6
Документация для результата лабораторных лабораторных работ №4 и №5, созданная по стандарту языка разметки [markdown](https://ru.wikipedia.org/wiki/Markdown)
Программа позваляет высчитать последовательность по Гипотезе Сиракуз (она же Гипотеза Коллатца) [markdown](https://ru.wikipedia.org/wiki/Гипотеза_Коллатца).

## Оглавление

1. [Функция высчета последовательности](#Функция высчета последовательности)
2. [Функция высчета максимума из последовательности](#Функция высчета максимума из последовательности)
3. [Тестирование](#Тестирование)
4. [Результаты тестирования](#Результаты тестирования)

## Функция высчета последовательности
Первая функция *syracuse_sequence* вычисляет последовательность Сиракуз по следующему алгоритму:
1) берём любое натуральное число N;
2) если оно чётное, то делим его на 2;
3) если оно нечётное, то умножаем на 3 и прибавляем 1 (получаем 3N + 1);
4) над полученным числом выполняем те же самые действия, и так далее.
Гипотеза Коллатца заключается в том, что какое бы начальное число n мы
ни взяли, рано или поздно мы получим единицу. 
Код функции:
```python
def syracuse_sequence(n):
    """
    Function to build Syracuse sequence
    :param n: number for building sequence
    :return: list of sequence
    """
    p_list = list()
    p_list.append(n)
    if n == 0:
        return []
    while n != 1:
        if n % 2 == 0:
            n = n / 2
            p_list.append(int(n))
        else:
            n = n * 3 + 1
            p_list.append(int(n))
    return p_list
```
____
[:arrow_up:Оглавление](#Оглавление)
____
## Функция высчета максимума из последовательности
Вторая функция *syracuse_max* вычисляет максимальный элемент из последовательности Сиракуз по следующему алгоритму:
1) берётся список из элементов последовательности, созданный функцией *syracuse_sequence*;
2) за изначальный максимальный элемент (max_n) берётся 0 (ноль);
3) проходимся по всему списку через цикл for ;
4) если попадается элемент больше max_n (i > max_n) - присваиваем max_n значение i элемента.
Код функции:
```python
def syracuse_max(n):
    """
    Function to find maximal element in Syracuse sequence
    :param n: number for building sequence
    :return: maximal element in Syracuse sequence
    """
    p_list = syracuse_sequence(n)
    max_n = 0
    for i in p_list:
        if i > max_n:
            max_n = i
    return max_n
```
____
[:arrow_up:Оглавление](#Оглавление)
____
## Тестирование
Тестирование программы через pytest:
```python
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
    ```
    Тестирование через unittest:
    ```python
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
```
____
[:arrow_up:Оглавление](#Оглавление)
____
## Резульаты тестирования
Ниже предоставлены результаты тестирования через pytest и unitest, а также пример вставки изображения:
![pytest](https://ibb.co/D1zYybd "100%")
![unittest](https://ibb.co/7QR2gqj "100%")

