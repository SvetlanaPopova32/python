my_f = open("text.txt", "w")

while True:
    content = (input())
    my_f.writelines(content + '\n')
    if content == " ":
        break
my_f.close()
