def say_hi():
    print("Hello User")

print("Top")
say_hi()
print("Bottom")

def say_hello(name, age): #say_hi function with name and age parameters
    print("Hello " + name + ", you are " + str(age))

say_hello("Mike", 35)
say_hello("Steve", 55)