class Animal:
    def __init__(self, name, sleep_duration):
        self.name = name
        self.sleep_duration = sleep_duration

    def sleep(self):
        print(
            "{} sleeps for {} hours".format(
                self.name,
                self.sleep_duration))
    
    def eat(self):
        print(f"{self.name} is eating")
    
    def drink(self):
        print(f"{self.name} is drinking")

# Note that the class Dog takes in Animal as a parameter!
class Dog(Animal):
    def bark(self):
        print("Woof! Woof!")

class Frog(Animal):
    def jump(self):
        print(f"{self.name} is jumping")


my_dog = Dog("Sophie", 12)
my_dog.sleep()
my_dog.bark()

froggie = Frog("Sheldon", 2)
froggie.jump()
froggie.eat()