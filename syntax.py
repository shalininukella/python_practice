from math import sqrt


print("shalini")
num = int(input("enter the numeber"))
sumi =  num + 12
print("sum is", sumi)
if num%2 == 0:
    print(num, " is even")

# Input: 10, 25, 15
# Output: Max is 25
numbers = [45,62,31,44,52]
n = len(numbers)
maxi = -1
for i in range(n):
    if numbers[i] > maxi:
        maxi = numbers[i]
print(maxi)

#or
print(max(numbers))

fruits = ["apple", "banana", "orange"]
# Output:
# apple
# banana
# orange

for i in fruits:
    print(i)

# Print 1 to N using for loop
n = int(input("enter n to loop till n"))
for i in range(n):
    print(i+1)

#or
n = int(input("Enter a numbe for looping till n : "))
for i in range(1, n + 1):
    print(i)


#Output: 50
#sum of the numbers
counting = [5, 10, 15, 20]
total = 0
for i in counting:
    total += i
print(total, " sum of the given numbers of the array")

#or 
numb = [5, 10, 15, 20]
total = sum(numb)
print("Sum:", total)


# Output: 3 even numbers
inp = [1, 2, 3, 4, 5, 6]
cnt = 0
for i in inp:
    if i%2 == 0:
        cnt += 1
print (cnt, " even numbers")

# 🟩 FUNCTIONS
# 9️⃣ Write a Function to Calculate Factorial of a Number
# Input: 5
# Output: 120
def fact(n):
    if n == 0 or n == 1:
        return 1
    
    return fact(n-1) * n

factorial = fact(5)
print(factorial, " factorial of 5")

#or
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

n = int(input("Enter a number: "))
print("Factorial:", factorial(n))


# 🔟 Function to Check if a Number is Prime
# Input: 7
# Output: Prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("Enter a number: "))
if is_prime(n):
    print("Prime")
else:
    print("Not Prime")


#or 
from math import sqrt
def prime(n):
    if n <= 1: 
        return False

    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

primeNum = prime(5)   
print(primeNum, "→ is 5 prime or not")




    

