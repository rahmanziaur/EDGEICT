import math 
from Circ import Circle

class DC:

  def __init__(self):
    pass
  
  def main(self):
    Circle.set_radius(10) #Change 1
    radius = Circle.get_radius()
    print(f"Area:{radius*radius*math.pi}")

    Circle.set_radius(25) #Change 2
    radius = Circle.get_radius()
    print(f"Area:{radius*radius*math.pi}")

    obj = Circle()
    print(obj._Circle__radius) 
    print(Circle._Circle__radius)