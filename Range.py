#Range

#The range() function is a built-in function in Python that returns a sequence of numbers, 
#starting from 0 by default, increments by 1 (also by default), and ends at a specified number.
# It's commonly used in loops to repeat an action a certain number of times 

print(list(range(5)))          # [0, 1, 2, 3, 4]

print(list(range(2, 5)))       # [2, 3, 4]

print(list(range(1, 8)))       # [1, 2, 3, 4, 5, 6, 7]

print(list(range(5, 3)))       # []

# Convert the range to a list and print it
numbers = list(range(10))
print(numbers)