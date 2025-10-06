def divide(a, b):
    return a / b

print("Starting...")
print(divide(5, 0))

#output
# Starting...
# Traceback (most recent call last):
#   File "c:\Users\NukellaShalini\python_practice\debugging\traceback.py", line 5, in <module>
#     print(divide(5, 0))
#   File "c:\Users\NukellaShalini\python_practice\debugging\traceback.py", line 2, in divide
#     return a / b
# ZeroDivisionError: division by zero


#explanation
# 👉 Let’s break it down:
# Traceback (most recent call last): → The error happened somewhere in your program.
# File "main.py", line 5, in <module> → The error started at line 5, in the main program.
# File "main.py", line 2, in divide → Inside the function divide, at line 2.
# ZeroDivisionError: division by zero → The exact error message.

# def divide(a, b):
#     return a / b

# print("Starting...")  # First print

# try:
#     print(divide(5, 0))  # This will cause an error
# except ZeroDivisionError as e:
#     print("Caught an error:", e)  # This will print when the error occurs
