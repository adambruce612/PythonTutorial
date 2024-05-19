employee_file = open(r"C:\Users\adam-\OneDrive\Documents\Python Tutorial\Reading Files\employees.txt", "w") #second argument means append, adding to the end 
#of the file
print(employee_file.write("\nKelly - Customer Service")) #\n will append to a new line
employee_file.close()