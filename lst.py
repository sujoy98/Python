lst = [1,2,3,4,5]
#newlst = [x+5 for x in lst]
newlst=[]
for x in range(len(lst)):
    newlst.append(lst[x] + 5)
print(newlst)
