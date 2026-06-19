#корутина

def fibbonacci():
    a, b = 0, 1
    while True:
        r = yield a
        print(f"Какой то шаблон для ответа: {r}\n")
        a, b = b, a + b


if __name__ == "__main__":
    coru = fibbonacci()

    n = int(input("Введите количество выведенных чисел ряда Фибоначчи: "))

    first_num = next(coru)
    print(f"Первое (потерянное) число: \n{first_num}")


    for i in range(n-1):
        num = coru.send(f"Какой то номер ответа {i}")
        print(num)



