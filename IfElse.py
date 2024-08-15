#If statements in Python allow you to execute certain code only if a certain condition is met.
# They are an important part of any programming language and are used frequently in Python

x = 10
if x > 5:
    print('x is greater than 5')

##If-else statements

#An if-else statement in Python is used to execute a block of code if a condition is True, 
#or a different block of code if the condition is False.

x = 10  

if x > 5:
    print('x is greater than 5')
else:
    print('x is not greater than 5')

##Comparison operators

#Comparison operators in Python allow you to compare two values and return a boolean value (True/False) based on the comparison. 
#They are an important part of any programming language and are used frequently in Python.

#Equal to (==): 

#Returns True if the values on either side of the operator are equal.
a = 5
b = 5
print(a == b)  # True, because 5 is equal to 5

#Not equal to (!=): 

#Returns True if the values on either side of the operator are not equal.
a = 5
b = 3
print(a != b)  # True, because 5 is not equal to 3

#Less than (<): 

#Returns True if the value on the left side of the operator is less than the value on the right side.
a = 3
b = 5
print(a < b)  # True, because 3 is less than 5

#Greater than (>): 

#Returns True if the value on the left side of the operator is greater than the value on the right side.
a = 7
b = 5
print(a > b)  # True, because 7 is greater than 5

#Less than or equal to (<=): 

#Returns True if the value on the left side of the operator is less than or equal to the value on the right side.
a = 5
b = 5
print(a <= b)  # True, because 5 is equal to 5

#Greater than or equal to (>=): 

#Returns True if the value on the left side of the operator is greater than or equal to the value on the right side.
a = 7
b = 5
print(a >= b)  # True, because 7 is greater than 5


## Elif

#The elif keyword in Python is short for "else if" and is used in conditional statements to handle multiple possible conditions. 
# It follows an if statement and is used to test additional conditions if the initial if condition is not met. 
#   Each elif block allows you to specify a new condition to test.

number = 15

if number > 20:
    print("The number is greater than 20.")
elif number > 10:
    print("The number is greater than 10 but not greater than 20.")
elif number > 0:
    print("The number is greater than 0 but not greater than 10.")
else:
    print("The number is 0 or negative.")
