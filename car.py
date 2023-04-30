class Car():
    def __init__(self, model, color, speed):
        self.model = "my_car"
        self.color = "my_color"
        self.speed = 0

    def accelerate(self, accels):
        self.speed += accels
        if (self.speed >= 100):
            self.speed = 100
            print(self.speed)
    
    def breaks(self, breaks):
        self.speed -= breaks
        if (self.speed <= 0):
            self.speed = 0
            print(self.speed)
    
    def get_speed(self):
        return self.speed


c = Car("tico", "red", 50)
c.accelerate(100)
c.breaks(120)
