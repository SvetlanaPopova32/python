with open ('text_3.txt', 'r', encoding='utf-8') as my_file:
    my_list = []
    for line in my_file:
        a = line. split()
        if float(a[1]) < 20000:
            print(a[0])
        my_list.append(float(a[1]))
print(sum(my_list)/len(my_list))