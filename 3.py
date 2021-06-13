class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt
res_list = []
while True:
    inp_data = input("Введите число: ")
    if inp_data == 'Stop':
        break
    try:
        try:
            inp_data = float(inp_data)
            res_list.append(inp_data)
        except:
            raise ValueError
    except:
        print("Вы ввели не число")

print(res_list)
