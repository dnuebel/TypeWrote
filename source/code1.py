number= input("How many integers do you want?")
lower_bound=input("What do you want all of your integers to be bigger than?")
upper_bound=input("What do you want all of your integers to be smaller than?")

import random
n= int(number)
count=1
while count<= n:
    x= random.randint(int(lower_bound) +1, int(upper_bound)-1)
    print (x)
    count= count+1
    
