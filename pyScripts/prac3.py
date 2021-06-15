num = int(input('Enter a range : '))
addVal = 0
if num < 0:
    print('Enter a whole positive number')
else:
    while num > 0:
        addVal = addVal+num
        num -= 1
print(f'sum of all numbers upto {num} is {addVal}')