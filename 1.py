from time import sleep


class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        while True:
            i = 0
            print(TrafficLight.__color[i])
            sleep(7)
            i += 1
            print(TrafficLight.__color[i])
            sleep(2)
            i += 1
            print(TrafficLight.__color[i])
            sleep(7)
 


t = TrafficLight()
t.running()