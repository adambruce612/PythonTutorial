phrase = "Giraffe Academy"
print(phrase)
print(phrase.upper().isupper()) #converts to uppercase and then returns boolean value if string is uppercase.
print(len(phrase)) #length of a string
print(phrase[0]) #0 indexed, will return G
print(phrase.index("G")) # will return index of G if it can be found, index function will throw an error if value cannot be found
print(phrase.replace("Giraffe", "Elephant")) #replaces Giraffe with Elephant