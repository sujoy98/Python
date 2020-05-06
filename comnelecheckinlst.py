a, b = [1,2,3,4,5], [3,1,6,7,2]
result = []
'''for i in a:
    if i in b:
        result.append(i)'''
result = [i for i in a if i in b] #list comprehension
print(result)

