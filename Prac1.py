def is_predicate_true(x):
    """
    Предикат: x^2 - 4 > 0
    """
    return x**2 - 4 > 0

def find_valid_domain(predicate, start, end, step=0):
    """
    Находит область определения предиката в заданном диапазоне.
    """
    valid_values = []
    x = start
    while x <= end:
        if predicate(x):
            valid_values.append(x)
        x += step
    return valid_values

def main():
    # Ввод значений для предиката и диапазона
    start = float(input("Введите начало диапазона: "))
    end = float(input("Введите конец диапазона: "))
    step = float(input("Введите шаг: "))

    # Находим значения, для которых предикат истинный
    valid_domain = find_valid_domain(is_predicate_true, start, end, step)
    print("Значения, для которых предикат истинный:", valid_domain)

if __name__ == "__main__":
    main()
