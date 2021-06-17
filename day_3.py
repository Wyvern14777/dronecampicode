import random

upperbound = int(input("what will the upperbound be"))
lowerbound = 1
randonumber = random.randint(lowerbound,upperbound)
randostring = str(randonumber)
GuessedNumber = input("guess the random number")
numberoftrys = 1
Winnmessage = ("you won")

while GuessedNumber != randostring :
    if GuessedNumber == ":)":
        print("nice you found a secret")
        break

    if GuessedNumber == "guesses":
        print (f"you have taken {numberoftrys} guesses")
        GuessedNumber = input(f"guess the random number, bounds are {lowerbound} to {upperbound}, guess again")
        continue
    GuessedNumber = int(GuessedNumber)
    if GuessedNumber > randonumber:
        print("to high,guess again")
        if upperbound > GuessedNumber:
            upperbound = GuessedNumber
    elif GuessedNumber < randonumber:
        print ("too low, guess again")
        if lowerbound < GuessedNumber:
            lowerbound = GuessedNumber
            
    numberoftrys +=1
    GuessedNumber = input(f"guess the random number, bounds are {lowerbound} to {upperbound}, guess again")
  
    
        
print(Winnmessage)
print(f"you took {numberoftrys} trys")







