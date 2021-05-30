from sys import argv
def salary(production, rate, bonus):
    return int(production) * int(rate) + int(bonus)

print(salary(argv[1], argv[2], argv[3]))