import math
import random
import time



    
event_array_veryrisky= [1.1,1.05,1.1,1.01,0.90,0.99,1.1]
myfunds = 100



x=myfunds
y=event_array_veryrisky

count=0
print("funds = {},  very risky scenario with big losses".format(x))
print("")


while(count<100):
    
    print("OPen {}".format(int(x)))
    print("")
    event = random.randint(0,6)

    x=x*y[event]

    print("cl0se{}".format(int(x)))
    print("")
   
    count += 1
    time.sleep(0.2)

