proceeds = float(input("Введите выручку"))
expenses = float(input("Введите издержки"))
if (proceeds - expenses > 0):
    print('Прибыль')
    profit = (proceeds-expenses)/proceeds
    print('Рентабельность выручки', profit)
    number_pers = int(input("Введите количество сотрудников"))
    print("Прибыль фирмы в расчете на одного сотрудника", profit/number_pers)

elif (proceeds - expenses < 0):
    print('Убыток')

#если бы убыток был меньше или равно, можно было через else
