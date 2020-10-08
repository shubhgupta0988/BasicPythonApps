'''Write a program which can compute the factorial of a given numbers.'''

def factorial (n):
    fact = 1
    if n == 0:
        return (1)
    else:
        return (n * factorial(n-1))

i = int(input("Enter the number whose factorial is to be found out:"))

print ("The factorial of the number is : ", factorial(i))
