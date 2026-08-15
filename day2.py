#Task1 Tokens and Statements
name = "Rahul"
age = 20
city = "Hyderabad"
print("Name: ", name)
print("Age: ", age)
print("City: ", city)

#Task2 Identifiers
name1 = "Akshith"
_age = 22
sub_marks = 95
print(name1)
print(_age)
print(sub_marks)
'''
Invalid Identifier because in variable creation we can not use special symbols expect underscore(_) 
@marks = 80
print(@marks)
 '''


#Task3 Single-line comments

name = "Varun"  # name is a variable and stores varun as value
age = 24   # age is a variable and stores 24 as value
print(name)
print(age)


#Task4 Multi-line comments

# This is a programs that describe a simple python program.
# It prints three messages on separate lines.
# The program uses the print() function to display the messages
print("Welcome to Python")
print("I am learning programming")
print("Python is easy to learn")

#Task5 Variables

name = "Akshith"
age = 22
height = 176
is_student = True
print(name)
print(age)
print(height)
print(is_student)

#Task6 Multiple Assignment

name, age, city = "Bhanu", 25, "Hyderabad"
print("Name: ", name)
print("Age: ", age)
print("City: ", city)

#Task7 Reassignment
age = 22
print(age)
age = 24
print(age)

#Task8 Swapping  Variables
a = 10
b = 20
print("Before: ", a, b)
a, b = b, a
print("After: ", a, b)

#Task9 Deleting Variables
name = "Akshith"
print(name)
del name
print(name)


#Task10 Keywords
import keyword
print("Python Keywords:")
print(keyword.kwlist)

print("Total: ", len(keyword.kwlist))