n=int(input('Enter a val: '))
# def fact_recr(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*fact_recr(n-1)
# print(fact_recr(n))

# 4 * fact_recr(4-1=3)
# 3 * fact_recr(3-1=2)
# 2 * fact_recr(2-1=1)
# 1 = 1*2*3*4 =24

def add_recr(n):
    if n==1:
        return 1
    elif n==0:
        return 0
    else:
        return n+add_recr(n-1)
print(add_recr(n))