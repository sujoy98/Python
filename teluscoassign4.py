for i in range(1,101):
    if not(i%3==0 or i%5==0):
        print(i)

# here we use continue statement

for i in range(1,101):
    if i%3==0 or i%5==0:
        continue
    print(i)


