class Animal:                                   #multilevel
    def eat(self):
        print("This animal is eating")

class prey(Animal):
    def flee(self):
        print("This animal is fleeing")

class preditor(Animal):
    def hunt(self):
        print("This animal is hunting")

class Rabbit(prey):
    pass

class Hawk(preditor):
    pass

rabbit = Rabbit()
hawk = Hawk()

print(rabbit.flee())