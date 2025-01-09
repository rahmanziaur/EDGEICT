class Circle:
    __radius = 0 # private attribute

    def __init__(self): #constructor
        pass

    @classmethod                #getter method, static
    def get_radius(cls):
        return cls.__radius

    @classmethod 
    def set_radius(cls, radius): #setter method
        cls.__radius = radius