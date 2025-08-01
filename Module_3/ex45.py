class Person(object):
    
    def __init__(self, name, age, eyes):
        self.name = name
        self.age = age
        self.eyes = eyes
    
    def talk(self, words):
        print(f"I am {self.name} and {words}")

becky = Person("Becky", 39, "green")
becky.talk("I am talking here!!")