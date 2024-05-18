is_male = True
is_tall = False

if is_male and is_tall: #you can also use the or keyword for comparing or
    print("You are a tall male")
elif is_male and not(is_tall): #else-if
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male but are tall")
else:
    print("You are either not a male and not tall")