def ageCheck():
    age = int(input("enter age > 18 "))
    if age < 18:
        raise ValueError("Age can't be less than 18 - this is written by me in the brackets of the ValueError which i manually raised for the 18 below condition. So no need of the except block")

ageCheck()