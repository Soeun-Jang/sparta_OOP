class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def speak(self):
        print("The animal speaks.")
        
class Dog(Animal):   
    def speak(self):
        print(f"Hi! I'm {self.name} and {self.age}years. 멍멍")
        
class Cat(Animal):
    def speak(self):
        print(f"Hi! I'm {self.name} and {self.age}years. 냥냥")

my_dog = Dog("Happy", 3)
my_dog.speak()
my_cat = Cat("Nabi", 2)
my_cat.speak()