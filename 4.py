class Cars:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, speed):
        if speed > 0:
            print("Машина поехала")

    def stop(self, speed):
        if speed == 0:
            print("Машина остановилась")

    def turn(self, direction):
        print(f"Машина повернула {direction}")

    def show_speed(self, speed):
        print(f"Скорость составляет {speed}")


class TownCar(Cars):
    def show_speed(self, speed):
        if self.speed > 60:
            print("Превышение скорости")


class SportCar(Cars):
    pass

class WorkCar(Cars):
    def show_speed(self, speed):
        if self.speed > 40:
            print("Превышение скорости")

class PoliceCar (Cars):
    pass

town = TownCar(70, 'black', "Zhiguli", False)
town.go(70)
town.stop(70)
town.turn('направо')
town.show_speed(70)


sport = SportCar(170, 'yellow', 'Ferrari', False)
sport.go(170)
sport.stop(170)
sport.turn('налево')
sport.show_speed(170)


work = WorkCar(36, 'white', 'Moskvich', False)
work.go(36)
work.stop(36)
work.turn('налево')
work.show_speed(36)


police = PoliceCar(130, 'white', "Ford", True)
police.go(130)
police.stop(130)
police.turn('направо')
police.show_speed(130)
