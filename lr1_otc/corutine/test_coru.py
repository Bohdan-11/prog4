import pytest
from corutine import fibbonacci


def test_fibonacci_sequence():
    """Проверяем, что корутина выдает правильную последовательность."""
    coru = fibbonacci()
    # Активация
    assert next(coru) == 0
    # Последовательные числа
    assert coru.send("step 1") == 1
    assert coru.send("step 2") == 1
    assert coru.send("step 3") == 2
    assert coru.send("step 4") == 3
    assert coru.send("step 5") == 5


def test_fibonacci_ignore_send_value():
    """Проверяем, что отправляемое значение не влияет на выдаваемые числа."""
    coru = fibbonacci()
    next(coru)  # 0
    # Отправляем разные значения, но получаем одну и ту же последовательность
    assert coru.send("any") == 1
    assert coru.send("value") == 1
    assert coru.send("does") == 2
    assert coru.send("not") == 3
    assert coru.send("matter") == 5


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
    """Проверяем n-е число Фибоначчи (начиная с 0-го)."""
    coru = fibbonacci()
    
    # Особый случай для n=0
    if n == 0:
        result = next(coru)  # просто активируем и получаем 0
    else:
        # Активируем корутину
        next(coru)  # получаем 0, но не используем
        
        # Пропускаем числа до n-1
        for _ in range(n - 1):
            next(coru)
        
        # Получаем n-е число
        result = coru.send(f"step {n}")
    
    assert result == expected


def test_fibonacci_long_sequence():
    """Проверяем, что корутина выдает правильные числа для больших индексов."""
    coru = fibbonacci()
    # Пропускаем первые 10 чисел
    for _ in range(10):
        next(coru)
    # 10-е число (индекс 10) = 55
    assert coru.send("long") == 55
    # 11-е = 89
    assert coru.send("long") == 89