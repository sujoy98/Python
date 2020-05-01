#153 is amstrong number because (1^3 + 5^3 + 7^3) = 153
num = int(input('Enter num to be checked : '))
temp = num
sum = 0

while(num>0):
    sum = sum + (num%10)*(num%10)*(num%10)
    num //= 10
    
if sum==temp:
    print('A number')
else:
    print('NA number')
    
    
    