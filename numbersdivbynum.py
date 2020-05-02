# Python Program to Find Numbers Divisible by Another Number
lst = [2, 4 ,23, 65, 78 ,100]
n = int(input('Enter a number to divide : '))
result = list(filter(lambda x: (x% n == 0), lst))
print(result)