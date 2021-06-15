myDict = {
    "A": 5+5,
    "B": 5-5,
    "C": [1,2,3,4],
    "D": (1,2,3,4),
    "E": {'hello':'world'}
}
# print(sum(myDict["C"]))
# print(myDict["D"])
# print(myDict["E"]['hello'])
# print(myDict.items())
for keys, values in myDict.items():
    print(keys,':',values)