# av as in aviable candies in the machine
av = 10
x = int(input('Enter the number of candies you want !! :'))
i=1
while i<=x:
    # we are checking with the stock of candies with av i.e aviable candies in the machine
    if i>av:
        print("~~~~OUT OF STOCK~~~~")
        break
    print("CANDY",i)
    i+=1
print("~~~~~BYE SEE YOU SOON~~~~~")
