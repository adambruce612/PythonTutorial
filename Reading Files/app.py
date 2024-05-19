employee_file = open(r"C:\Users\adam-\OneDrive\Documents\Python Tutorial\Reading Files\employees.txt", "r")
 # second argument is how to open the file. r is read, w is write, a is append, r+ is read and write

print(employee_file.readable()) #.readable function returns Boolean value if file is readable
#print(employee_file.read()) #reads the file
#print(employee_file.readline()) #reads a line from the file (in this example the first line, moving the cursor to the beginning of the second line)
#print(employee_file.readlines()) # takes all the lines in a file and puts them into an array
#print(employee_file.readlines()[1]) # lines in the file can be accessed in the same way an array element would be accessed

for employee in employee_file.readlines():
    print(employee)
 
employee_file.close() # best practice is to close a file after opening it