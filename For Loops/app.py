friends = ["Jim", "Karen", "Kevin"]


for letter in "Giraffe Academy":
    print(letter)

for name in friends:
    print(name)

for index in range(3,10): #prints all numbers between 3 and 10 not including 10
    print(index)

for index in range(len(friends)):
    print(friends[index])

for index in range(5):
    if index == 0:
        print("first iteration")
    else:
        print("Not first")