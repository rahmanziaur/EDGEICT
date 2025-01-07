from TestDog import TestDog 

class DriverClass:
  def main(self):
    rw = TestDog("Rat Wheller", 5)
    rw.printDogInfo()
  
  # def __init__(self):
  #    pass
  
if __name__=="__main__":
    dc = DriverClass()
    dc.main()