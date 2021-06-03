

my_dict = {}
with open('text_6.txt', encoding='utf-8') as my_file:
    for line in my_file:
        my_list = line.split(' ')
        i = 0
        for item in my_list:
            if item.isdigit() == True:
                i += int(item)
        my_dict[my_list[0]] = i
print(my_dict)