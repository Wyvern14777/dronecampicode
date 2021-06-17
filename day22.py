from day_2 import DaysToThirty,Camp

def ChooseFunction():

    Choose = input(" witch function would you like")

    if Choose == "Camp": 
        Camp()
    elif Choose == "DaysToThirty": 
        DaysToThirty()
    else:
        print("wrong")
        ChooseFunction()
ChooseFunction()







