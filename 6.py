goods_lst = []
number = 1
i = 1
while True:
    goods_lst.append((number, (dict({'название': input("Введите название товара"), 'цена': float(input("Введите цену")), 'количество': int(input("Введите количество")), 'ед': input("Введите единицы измерения")}))))
    number+=1
    i+=1
    if input("Данный товар внесен в список. Завершить добавление?") == 'да':
        break
print(goods_lst)

# не получилось сделать так, чтобы каждый кортеж добавлялся в список с новой строки. пробовала добавлять после кортежа \n и т.д., но код от этого не работает вообще