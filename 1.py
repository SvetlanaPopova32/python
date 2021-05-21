def first_func():
    try:
        var_1 = float(input("Введите первое число"))
        var_2 = float(input("Введите второе число"))
        return var_1 / var_2
    except ZeroDivisionError:
        return

print(first_func())