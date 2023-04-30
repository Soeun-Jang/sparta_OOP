class Animal:
    def __init__(self):
        pass
    def speak(self):
        print("The animal speaks.")
        
class Dog(Animal):   
    def speak(self):
        print("Woof!")
        
class Cat(Animal):
    def speak(self):
        print("Meow!")

my_dog = Dog()
my_dog.speak()