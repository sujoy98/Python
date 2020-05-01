# sum of natural numbers

num = int(input('Enter range of natural numbers : '))
total = 0
for i in range(1,num):
    if i<=0: print('Natural number starts from 1 ')
    else:
        total += i

print('Sum of the Natural numbers within {} is {}'.format(num,total))
    
    
        
    