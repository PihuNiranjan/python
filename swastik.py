n=5
i=1
print("")
while i<=n:
   if i==1:
       j=1
       while j<=5:
           if j==2:
              print("     ",end="")
           else:
              print("#    ",end="")
           
           j+=1
  
   if i==2:
        j=1
        while j<=5:
            if j==1 or j==3:
                print("#    ",end="")
            else:
                print("     ",end="")
            j+=1

   if i==3:
       j=1
       while j<=5:
           print("#    ",end="")
           j+=1
  

   if i==4:
       j=1
       while j<=5:
           if j==3 or j==5:
               print("#    ",end="")
           else:
               print("     ",end="")
           j+=1

  
   if i==5:
        j=1
        while j<=5:
            if j==4:
                print("     ",end="")
            else:
                print("#    ",end="")
            j+=1

   i+=1 
   print("")   
    
    