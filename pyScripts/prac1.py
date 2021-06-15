myDict = {
    'Pankha': 'Fan',
    'Dabba': 'Box',
    'Vastu' : 'Item'
}
print(list(myDict.keys()))
word = input('Enter a HINDI word to find meaning : ')

# key error if key is not founf
# print('The meaning of',word,'in ENGLISH is',myDict[word])

# returns NONE if key is not found
print('The meaning of',word,'in ENGLISH is',myDict.get(word))