def divide(a, b):
    return a / b

print("Starting...")  # First print

try:
    print(divide(5, 0))  # This will cause an error
except ZeroDivisionError as e:
    print("Caught an error:", e)  # This will print when the error occurs
