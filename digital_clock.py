from threading import *
import time
import os
def clock():
  for h in range(24):
    for m in range(60):
      for s in range(60):
        print("HH : MM : SS")
        print(h,": ",m,": ",s)
        time.sleep(1)
        clear = lambda : os.system('cls')
        clear()
t=Thread(target=clock)
t.start()

        