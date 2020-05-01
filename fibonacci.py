n = int(input('enter range '))
def fib(n):
    a=0
    b=1
    
    if n==1:
        print(a)
    else:
        print(a)
        print(b)

        for i in range(2,n):
# we need to swap the num for printing the next value         
            c = a+b
            a = b
            b = c
            print(c)
            
print(fib(n))
