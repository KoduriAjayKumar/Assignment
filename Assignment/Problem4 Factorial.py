#To find the factorial of a number using recursion.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
num = int(input())
#If the number is negative factorial is undefined
if num < 0:
    print("For negative numbers the factorial is undefiend.")
else:
    print("The factorial of",num,"is : ",factorial(num))