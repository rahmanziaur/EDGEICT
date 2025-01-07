class TestDog: #class name Dog, ended with a colon
    species = "Canine"  # Class attribute, class variable

    def __init__(self, name, age): #constructor, it has 
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute
    
    def printDogInfo(self):
      print(f"Name:{self.name}\n Age:{self.age}")