import pytest
from iter_next import FIB_ITER  

def test_fibonacci_sequence():
    """Проверяем, что итератор выдаёт правильные первые числа."""
    f = FIB_ITER(max=10)
    expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    result = list(f)  # собираем все элементы до StopIteration
    assert result == expected


def test_fibonacci_manual_next():
    """Проверяем последовательность через ручные вызовы next()."""
    f = FIB_ITER(max=7)
    assert next(f) == 0
    assert next(f) == 1
    assert next(f) == 1
    assert next(f) == 2
    assert next(f) == 3
    assert next(f) == 5
    assert next(f) == 8
    # следующий вызов должен выбросить StopIteration
    with pytest.raises(StopIteration):
        next(f)


@pytest.mark.parametrize("n, expected", [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    (7, 13),
])
def test_fibonacci_nth_number(n, expected):
    """Проверяем n-е число, получая его через последовательные next()."""
    f = FIB_ITER()  # без max, бесконечный
    # Пропускаем первые n чисел
    for _ in range(n):
        next(f)
    # Теперь текущее значение - n-е число
    assert next(f) == expected


def test_fibonacci_max_stop():
    """Проверяем, что итерация останавливается на max."""
    f = FIB_ITER(max=5)
    result = []
    for num in f:
        result.append(num)
    assert result == [0, 1, 1, 2, 3]
    # После завершения for, итератор исчерпан
    with pytest.raises(StopIteration):
        next(f)


def test_fibonacci_no_max_infinite():
    """Проверяем, что без max итератор выдаёт бесконечную последовательность.
    В тесте мы не можем проверить бесконечность, но можем взять первые 10 чисел и убедиться, что они верны.
    """
    f = FIB_ITER()  # max=None
    first_10 = [next(f) for _ in range(10)]
    assert first_10 == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


def test_fibonacci_reset_state():
    """Проверяем, что создание нового итератора сбрасывает состояние."""
    f1 = FIB_ITER(max=3)
    assert list(f1) == [0, 1, 1]  # исчерпан

    # Создаём новый объект
    f2 = FIB_ITER(max=3)
    assert list(f2) == [0, 1, 1]  # снова работает


def test_fibonacci_large_numbers():
    """Проверяем, что итератор правильно вычисляет большие числа."""
    f = FIB_ITER()
    for _ in range(20):
        next(f)
    assert next(f) == 6765
    assert next(f) == 10946  

def test_fibonacci_iter_multiple_for():
    """Проверяем, что повторный for на том же объекте ничего не даёт."""
    f = FIB_ITER(max=5)
    assert list(f) == [0, 1, 1, 2, 3]
    # Второй раз список будет пуст, так как итератор исчерпан
    assert list(f) == []