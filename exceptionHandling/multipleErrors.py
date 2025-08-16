def multipleIndividulaErrors():
    try:
        print('from multipleIndividulaErrors function')
        num = int(input("enter the number which i'm gonna use for dividing 10 - "))
        10 / num
    except ValueError as e:
        print(f"runs when the input is invalid like num = int('12a'). And now the actual error's description thrown by ValueError is '{e}'")
    except ZeroDivisionError as e:
        print(f"'{e}' - is the error thrown by ZeroDivisionError")
    finally:
        print('finally block - always runs')


# or group the multiple errors 
def groupingExceptions():
    try:
        print('from groupingExceptions function')
        num = int(input("enter the number which i'm gonna use for dividing 10 - "))
        10 / num
    except (ValueError, ZeroDivisionError) as e:
        print(f"Error is '{e}'")
    finally:
        print('finally block - always runs')
        
multipleIndividulaErrors()
groupingExceptions()
