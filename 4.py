def my_func(a, b):
    return 1/a ** abs(b)
print (my_func(4, -5))


def my_func(a, b):
    i = 1
    k = a
    while i < abs(b):
        c = k * a
        k = c
        i+=1
    d = 1 / c
    return d
print(my_func(4, -5))