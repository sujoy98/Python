a, b = [1, 2, 3, 4, 5], [6, 7, 8, 9, 10]
#taking two list
'''z =[] # taking z as an empty list to store the resultant list
for i in range(len(a)): #we need to tale len of a or b anyone
    z.append(a[i]*b[i]) #returns the product of two list'''
z = [a[i]*b[i] for i in range(len(a))]
print(z)
