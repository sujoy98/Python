#153 is amstrong number because (1^3 + 5^3 + 7^3) = 153

lower = int(input('Enter lower range : '))
upper = int(input('Enter upper range : '))

for num in range(lower, upper+1):
    temp = num
    sum = 0
    while(num>0):
            sum = sum + (num%10)*(num%10)*(num%10)
            num //= 10
            if sum==temp:
                print(sum)
            
        
                
        

        