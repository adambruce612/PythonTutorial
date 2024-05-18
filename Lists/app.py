friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"] #lists can contain different data types and are zero indexed

print(friends)
print(friends[0])
print(friends[-1]) # a negative starts indexing from the back of the list. When coutning backwards the last index is -1.
print(friends[1:]) #this will print starting at index 1 through the end of the list.
print(friends[1:3]) # prints the range from index 1-3

friends[1] = "Mike"
print(friends[1])