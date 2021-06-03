dict_1 = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('text_4(1).txt', 'r', encoding='utf-8') as my_file:
    for line in my_file:
        one_line = line.split(' ')
        one_line[0] = dict_1[one_line[0]]
        print(one_line)
        with open('text_4(2).txt', 'a', encoding='utf-8') as my_file_2:
            my_file_2.writelines(one_line)


