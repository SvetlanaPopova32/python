with open('text_5.txt', 'w') as my_file_1:
    my_file_1.writelines(input())



with open('text_5.txt', 'r') as my_file:
    numbers = (my_file.readline().split(' '))
    my_list = []
    for number in numbers:
        my_list.append(int(number))
    print(sum(my_list))
