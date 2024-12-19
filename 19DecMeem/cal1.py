# defining a function to add two numbers 

def add(a=0, b=0):
     return a + b
# taking two inputs from keyboard

a = int(input("Enter a:"))
b = int(input("Enter b:"))

#printing the sum and calling the function

print(a, " + ",b," = ",add(a,b))