lst_1 = [int(i) for i in input().split()]
if len(lst_1) % 2 != 0:
    j = 0
    while j < len(lst_1) - 2:
        lst_1[j], lst_1[j + 1] = lst_1[j + 1], lst_1[j]
        j += 2
else:
    j = 1
    while j <= len(lst_1) - 1:
        lst_1[j], lst_1[j-1] = lst_1[j-1], lst_1[j]
        j += 2
print(lst_1)