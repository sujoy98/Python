num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))
num4 = int(input("Enter a number: "))

greatest = num1
if(num2 > num1) and (num2 > num3) and (num2 > num4):
    greatest = num2
elif(num3 > num2) and (num3 > num4):
    greatest = num3
else:
    greatest = num4

print('Gretest is',greatest)