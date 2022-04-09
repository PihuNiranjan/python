def sugar():  
  sum=0 
  n=float(input("Enter your quantity of sugar: "))
  sum=n*10
  print("\n","       Quantity      rate per kg    total amount" )
  print("\n","\t",n,"    \t","10  ","   \t",sum)
  print("\n","\tplease pay : ",sum)

def floar():
  sum=0 
  n=float(input("Enter your quantity of floar: "))
  sum=n*8
  print("\n","       Quantity      rate per kg    total amount" )
  print("\n","\t",n,"    \t","10  ","   \t",sum)
  print("\n","\tplease pay : ",sum)

def tea():
  sum=0 
  n=float(input("Enter your quantity of tea: "))
  sum=n*15
  print("\n","       Quantity      rate per kg    total amount" )
  print("\n","\t",n,"    \t","10  ","   \t",sum)
  print("\n","\tplease pay : ",sum)

def rice():
  sum=0 
  n=float(input("Enter your quantity of rice: "))
  sum=n*12
  print("\n","       Quantity      rate per kg    total amount" )
  print("\n","\t",n,"    \t","10  ","   \t",sum)
  print("\n","\tplease pay : ",sum)

def wheat():
  sum=0 
  n=float(input("Enter your quantity of wheat: "))
  sum=n*5
  print("\n","       Quantity      rate per kg    total amount" )
  print("\n","\t",n,"    \t","10  ","   \t",sum)
  print("\n","\tplease pay : ",sum)

while(True):
  print("\nAvailable products are:-")
  print("\n 1 for sugar\n 2 for floar\n 3 for tea\n 4 for rice\n 5 for wheat")
  print(" 6 for Exit")
  p=int(input("choose your product: "))

  if(p==1):
    sugar()
  elif(p==2):
    floar()
  elif(p==3):
    tea()
  elif(p==4):
    rice()
  elif(p==5):
    wheat()
  elif(p==6):
    break
  else:
    print("your are wrong person.... ")
  
  
  