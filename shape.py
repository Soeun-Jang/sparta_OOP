class Shape:
    def get_area(self):
        pass
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2
    
class Square(Shape):
      def __init__(self, side):
          self.side = side
      def area(self):
         return self.side ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

circle = Circle(20)
print(circle.area())

square = Square(10)
print(square.area())

rectangle = Rectangle(20, 40)
print(rectangle.area())