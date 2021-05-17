a = int(input())
max_num = 9
while a // 10 > 0:
    if max_num < a % 10:
        max_num = a % 10
    a = a // 10
print (max_num)



