def add():
  a=float(input("Enter first number: "))
  b=float(input("Enter second number: "))
  c=a+b       
  print("Result = ",c)

def sub():
  a=float(input("Enter first number: "))
  b=float(input("Enter second number: "))
  c=a-b       
  print("Result = ",c)

def multi():
  a=float(input("Enter first number: "))
  b=float(input("Enter second number: "))
  c=a*b       
  print("Result = ",c)

def div():
  a=float(input("Enter first number: "))
  b=float(input("Enter second number: "))
  c=a/b       
  print("Result = ",c)

def floar():
  a=float(input("Enter first number: "))
  b=float(input("Enter second number: "))
  c=a//b       
  print("Result = ",c)

def mod():
  a=float(input("Enter first number: "))
  b=float(input("Enter second number: "))
  c=a%b       
  print("Result = ",c)






while(True):
  print("\nChoose your choice: ")
  print(" 1 for Addtion\n 2 for Subtraction\n 3 for Multiplication\n 4 for Division \n 5 for floar\n 6 for modulus")
  print(" 7 for Exit")
  n=float(input("Enter your choice: "))
  
  if(n==1):
    add()

  elif(n==2):
    sub()
    
  elif(n==3):
    multi()

  elif(n==4):
    div()
 
  elif(n==5):
    floar()
 
  elif(n==6):
    mod()

  elif(n==7):
    break

  else:
    print(" your are wronge person...")

    