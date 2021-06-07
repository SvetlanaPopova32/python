class Road:

    def __init__(self, length, width, height):
        self._length = length
        self._width = width
        self.height = height
        self.weight = 10


    def asphalt_mass(self):
        asphalt_mass = self._length * self._width * self.weight * self.height/1000
        print(asphalt_mass, 'т')


road_1 = Road(5000, 20, 5)
road_1.asphalt_mass()