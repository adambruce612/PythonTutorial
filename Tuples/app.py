#tuples are a data structure, similar to a list but with the differences:
# tuples are immutable (can't be changed or modified)
# indexed starting at 0
# 

coordinates = (4, 5) # 4 is index 0, 5 is index 1
# coordinates[1] = 10 #will throw an error since a tuple is immutable
print(coordinates[0])