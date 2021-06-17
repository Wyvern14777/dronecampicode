def Camp():
    CampName = input("what is your camps name ")
    print(CampName)
    NumDays = int(input("how many days is it "))
    print(NumDays)
    CurrentDay = int(input("what is the current day of camp"))
    DaysLeft = NumDays - CurrentDay
    print(f"thare are {DaysLeft} days left in {CampName}")


def DaysToThirty():
    CurrentYears = int(input("how many years old are you please include days"))
    print(CurrentYears)

    Years = 30 - CurrentYears 

    DaysTillThirty = 365*Years
    print(f"number of days till you are 30 {DaysTillThirty}")


































































