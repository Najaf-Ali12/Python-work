'''Task 1: Animal Kingdom
- Create an Animal class with attributes like name, age, and sound.
- Create subclasses like Dog, Cat, and Bird that inherit from Animal.
- Each subclass should have its own unique behavior (e.g., Dog can bark, Cat can meow, Bird can chirp
).
'''
class Animal:
    #following work as constructor in python. At the place of self any word can be used
    def __init__(animalproperities,name,age,sound):   #here name,age and sound variables are just declared not initialized yet
        animalproperities.name=name
        animalproperities.age=age
        animalproperities.sound=sound
    def makeSound(animalmethods):
        print("Animal makes sound")

    #in python syntax of inheritance is ChildClass(ParentClass)
class Dog(Animal):
    def __init__(dogproperities,name,age,sound):
        dogproperities.name=name
        dogproperities.age=age
        dogproperities.sound=sound
    def makeSound(dogmethods):
        print("The name of dog is",dogmethods.name)
        print("The age of dog is",dogmethods.age)
        print("Dog",dogmethods.sound)
class Cat(Animal):
    def __init__(Catproperities,name,age,sound):
        Catproperities.name=name
        Catproperities.age=age
        Catproperities.sound=sound
    def makeSound(catmethods):
        print("The name of cat is",catmethods.name)
        print("The age of cat is",catmethods.age)
        print("The cat does",catmethods.sound)
class Bird(Animal):
    def __init__(birdproperities, name, age, sound,speed):
        super().__init__(name,age,sound)
        birdproperities.speed=speed
    def makeSound(birdmethods):
        print("The name of bird is",birdmethods.name)
        print("The age of bird is",birdmethods.age)
        print("The birds",birdmethods.sound)
        print("Speed of",birdmethods.name,"is",birdmethods.speed)
#creating an object of subclasses Dog,Cat,Bird
object=Dog("Tomy",5,"Barks")
object.makeSound()
print()
object2=Cat("Khiri","2years","meow meow")
object2.makeSound()
print()
object3=Bird("Shaheen","1.5 years","Chirps","190km/sec")
object3.makeSound()