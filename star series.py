#python 3
n=int(input("enter number of series : "))
i=1
while i<=n:
  j=1
  while j<=i:
    print("*",end="  ")
    j+=1
  i+=1
  print("")

i=n-1
while i>=1:
  j=1
  while j<=i:
    print("*",end="  ")
    j+=1
  i-=1
  print("")