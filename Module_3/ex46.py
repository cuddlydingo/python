## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a Animal
class Dog(Animal):
    def __init__(self, name):
        ## Dog has-a name
        self.name = name

## Cat is-a Animal
class Cat(Animal):
    def __init__(self, name):
        ## Cat has-a name
        self.name = name
        
## Person is-a object
class Person(object):
    def __init__(self, name):
        ## Person has-a name
        self.name = name
        
        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a Person
class Employee(Person):
    def __init__(self, name, salary):
        ## super has-a name
        super(Employee, self).__init__(name)
        ## employee has-a salart
        self.salarty = salary
        
## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon (Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish): 
    pass

## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a person
mary = Person("Mary")

## Mary has-a pet
mary.pet = satan

## frank is-a employee
frank = Employee("Frank", 120000)

## frank has a pet
frank.pet = rover

## flipper is a Fish
flipper = Fish()

## crouse is a salmon
crouse = Salmon()

## harry is a halibut
harry = Halibut()