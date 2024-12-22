import SimCal as s

while True:
  print("Enter 1 to add, \n2 to subtract, \n3 to multiplication and \n4 for division\n 0 to exit")

  choice = int(input("Your Choice:"))

  if choice ==0:
     break
    
  if choice==1:
     a = int(input("Enter a:"))
     b = int(input("Enter b:"))
     print(s.add(a,b))
  if choice==2:
     a = int(input("Enter a:"))
     b = int(input("Enter b:"))
     print(s.sub(a,b))
  if choice==3:
     a = int(input("Enter a:"))
     b = int(input("Enter b:"))
     print(s.mul(a,b))
  if choice==4:
     a = int(input("Enter a:"))
     b = int(input("Enter b:"))
     print(s.div(a,b))
   

 