with open("text_2.txt", "r") as f_obj:
    i = 0
    for line in f_obj:
        my_list = line.split()
        print("количество слов в строке", len(my_list))
        i += 1
print("Количество строк", i)


