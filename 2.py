class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

inp_data_1 = int(input("Введите числитель "))
inp_data_2 = int(input("Введите знаменатель: "))

try:
    res = inp_data_1 / inp_data_2
    print(f"Результат деления: {res}")
except ZeroDivisionError:
    print("На ноль делить нельзя!")
