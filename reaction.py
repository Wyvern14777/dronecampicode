
import random
import time
reactnum = random.randint(1,10)
secounds = int(input("how fast "))
print(reactnum)
time.sleep (secounds)
for i in range(30):
    print()
m=random.randint(1,10)
while m < 12:
    print (m)
    reaction = input("is this your number? ")
    if reaction == "yes":
        if reactnum == m:
            print ("you win ")
            m = 11
        else:
            print ("nope")
            m = 11
    elif reaction == "no":
        m=random.randint(1,10)















