num = int(input("Enter a number to check for prime : "))
prime = True
for i in range(2,num):
    if(num%i == 0):
        prime = False
        break
if prime:
    print(f'{num} is a prime number')
else:
    print(f'{num} is not a prime number')