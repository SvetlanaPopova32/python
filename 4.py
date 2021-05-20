lst_1 = [(i) for i in input().split()]
j = 0
n = 1
for j in range(0, len(lst_1)):
    print(n, "{:.10}".format(lst_1[j]))
    j +=1
    n +=1


