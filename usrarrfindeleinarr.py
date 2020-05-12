from array import *
arr = array('i', [])
size = int(input('Enter the Size of the array : '))
for i in range(size):
    x = int(input('Enter the value :'))
    arr.append(x)
print(arr)

vals = int(input('Enter the  value to be search : '))
k = 0
for e in arr:
    if e == vals:
        print('Searched value in index', k)
    k += 1
    #break we ca use break if we want to display the first occurance
# if we want to use function
print(arr.index(vals)) # this will return the first occurance in default

