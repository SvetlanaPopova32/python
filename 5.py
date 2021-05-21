def funct_5():
    result = 0
    while True:
        value = ([(i) for i in input().split()])
        i = 0
        k = 0
        for i in range(len(value)):
            if value[i] == '#':
                break
            sum_1 = int(value[i]) + k
            k = sum_1
            i += 1
        result += sum_1
        print(result)
funct_5()


