#Lists

#In Python, a list is a mutable, ordered collection of items.
#  Lists are one of the most versatile data structures in Python and can hold a mix of data types.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Create a list from a string

chars = list('hello')
print(chars)  # ['h', 'e', 'l', 'l', 'o']

#Adding elements to a list with the append method

names = ['Anna', 'Bob']
print(names)              # ['Anna', 'Bob']

names.append('Simon')     # ['Anna', 'Bob', 'Simon']
print(names)

names.append('Lily')
print(names)              # ['Anna', 'Bob', 'Simon', 'Lily']