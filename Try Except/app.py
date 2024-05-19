# try except in Python is the same as try-catch in other languages
try:
    value = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err: #saves error as variable
    print(err) 
except ValueError:
    print("Invalid input")

