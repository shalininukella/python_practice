class CustomException(Exception):
    pass

def functionToRaiseMyCustomException():
    age = int(input("enter the age > 9"))
    if age < 9:
        raise CustomException("From my custom exception - age shouldn't be less than 9")

functionToRaiseMyCustomException()