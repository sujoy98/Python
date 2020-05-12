from array import*
arr = []
size = int(input('enter the size of the array : '))
for i in range(size):
    x = int(input('enter next value : '))
    arr.append(x)
print(arr)

vals = int(input('enter the index of the number to be deleted : '))
del arr[vals]
print(arr)
