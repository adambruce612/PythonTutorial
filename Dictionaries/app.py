monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(monthConversions["Nov"]) #values can be accessed by passing in the key
print(monthConversions.get("Luv", "Not a valid key")) #same as above but can take a default value if key is not found (the second argument)
