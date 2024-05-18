lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]

print(friends)

 #friends.extend(lucky_numbers) # adds lucky_numbers list to the end of the friends list
friends.append("Creed") # appends an item to the end of the list
friends.insert(1, "Kelly")
friends.remove("Jim") #removes an element from the list
friends.clear() #empties the list
friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]
friends.pop() # removes the last element from the list
print(friends)

print(friends.index("Kevin")) # will return index of value if found. If not found, an error will be thrown

print(friends.count("Jim")) #will print how many times an element appears in the list

friends.sort() #sorts the list is ascending order (or alphabetical)

lucky_numbers.sort() #sorts the list in ascending order
lucky_numbers.reverse() # reverse a list
print(lucky_numbers)
 
friends2 = friends.copy() # copies friends list
print(friends2)