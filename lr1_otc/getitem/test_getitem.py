import pytest
from getitem import FIB_ITER  


def test_fibonacci_sequence():
    """Проверяем, что обращение по индексам даёт правильную последовательность."""
    f = FIB_ITER(max=10)
    assert f[0] == 0
    assert f[1] == 1
    assert f[2] == 1
    assert f[3] == 2
    assert f[4] == 3
    assert f[5] == 5
    assert f[6] == 8
    assert f[7] == 13


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
    """Проверяем n-е число через прямой доступ."""
    f = FIB_ITER(max=20)  # достаточно большой max
    assert f[n] == expected


def test_fibonacci_iteration_with_max():
    """Проверяем, что итерация останавливается на max."""
    f = FIB_ITER(max=5)
    result = list(f)  # Python будет вызывать __getitem__ с 0,1,2,3,4, затем IndexError и остановится
    assert result == [0, 1, 1, 2, 3]


def test_fibonacci_max_index_error():
    """Проверяем, что при index >= max выбрасывается IndexError."""
    f = FIB_ITER(max=5)
    with pytest.raises(IndexError):
        _ = f[5]  # индекс равен max -> ошибка
    with pytest.raises(IndexError):
        _ = f[10]


def test_fibonacci_no_max_infinite_iteration():
    """Проверяем, что без max итерация была бы бесконечной.
    В тесте мы не можем проверить бесконечность, но можем проверить, что первые несколько чисел верны.
    """
    f = FIB_ITER()  # max=None
    # Возьмём первые 10 чисел вручную, чтобы убедиться, что они правильные
    first_10 = [f[i] for i in range(10)]
    assert first_10 == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    # При этом важно помнить, что for f будет бесконечным – это поведение документировано или оговорено.


def test_fibonacci_large_index():
    """Проверяем вычисление для большого индекса (без max)."""
    f = FIB_ITER()
    assert f[20] == 6765
    assert f[30] == 832040