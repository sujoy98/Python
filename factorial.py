'''def factorial(n):

    if (n == 0):
        return 1
    else:
        return n * factorial(n-1)

print(factorial(4))'''


from math import factorial
n = int(input('Enter the number to find factorial : '))
fac = factorial(n)
print(fac)


