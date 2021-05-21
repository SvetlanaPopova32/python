def my_func (a, b, c):
    lst = [a, b, c]
    lst.remove(min(lst))
    return lst[0] + lst[1]
print (my_func(5, 7, 15))

