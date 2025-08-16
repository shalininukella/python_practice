#Runs if no exception was raised in try:

try:
    num = int(input("enter the number"))
    10/num
except ZeroDivisionError:
    print("cant divide by 0")
else:
    print("runs only when exception wasn't raised. So if you are seeing this message - hehe no ZeroDivisionError caused, peace!")
finally:
    print("alwyas - finally block. And yes, finally can't be written before else, Else is for Try, so writing finally before else will cause a SyntaxError...")

