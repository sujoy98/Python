num = int(input("Enter a number to be checked :"))
for i in range(2, num):
    if num % i == 0:
        print("NOT PRIME")
        break
else: # using FOR-ELSE
    print("PRIME")

'''if we dont want to use for else then

num = int(input("Enter a number to be checked :"))
for i in range(2, num):
    if num % i == 0:
        print("NOT PRIME")
        break
    else:
        print("PRIME")
        break '''
