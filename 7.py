import json
my_dict = {}
sum_profit = 0
i = 0
with open('text_7.txt', encoding='utf-8') as my_file:
    for line in my_file:
        my_list = line.split(' ')
        profit = int(my_list[2]) - int(my_list[3])
        my_dict[my_list[0]] = profit
        if profit > 0:
            sum_profit += profit
            i += 1
my_dict_2 = {
'average_profit': sum_profit/i
}
print([my_dict], [my_dict_2])
data = [my_dict], [my_dict_2]

with open("my_file.json", "w") as write_f:
    json.dump(data, write_f)