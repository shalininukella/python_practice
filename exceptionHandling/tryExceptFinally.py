try:
    1/0
except ZeroDivisionError as e:
    print(f"'{e}' is the error's description")
finally:
    print("finally block - always runs")