class Dog:
  species = "canine"

  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def printM(self):
    print(f"Name:{self.name}\n Age:{self.age}")
