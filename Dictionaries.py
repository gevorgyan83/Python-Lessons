#Dictionaries

#Python dictionaries are a powerful 
#and versatile data structure that can be used to store and organize data in a way that is easy to access and modify. 
#They are similar to lists but, instead of using numerical indexes to access items, dictionaries use keys.

# Create a dictionary with predefined values
grades = {'John': 'A', 'Anna': 'B', 'Bob': 'C'}

# Create an empty dictionary and add values one by one
grades = {}
grades['John'] = 'A'
grades['Anna'] = 'B'
grades['Bob'] = 'C'

#Accessing Items in a Python Dictionary
#Similar to lists, to access an item in a dictionary, we use the key in square brackets []:

print(grades['John'])   # 'A'
print(grades['Bob'])    # 'C'
print(grades['David'])  # KeyError

#If we try to access a key that does not exist in the dictionary, it will raise a KeyError. 
#To avoid this, we can use the get() method, which returns None if the key does not exist, 
#or the default value if we provide as a second argument:

print(grades.get('Tom'))          # None
print(grades.get('David', 'F'))   # 'F'
print(grades.get('Bob', 'F'))     # 'C'

#Modifying Items in a Python Dictionary

grades = {'John': 'A', 'Anna': 'B', 'Bob': 'C'}

# Imagine there was a mistake in the reference answers of a test
# We need to update the grades for some students
grades['John'] = 'B'      # Oops the grade was lowered
grades['Anna'] = 'A'      # Anna's answer was actually correct
print(grades)             # {'John': 'B', 'Anna': 'A', 'Bob': 'C'}

#Adding Items To The Dictionary

grades = {'John': 'A', 'Anna': 'B', 'Bob': 'C'}
grades['David'] = 'A'
grades['John'] = 'B'
grades['Simon'] = 'C'
print(grades)
# {'John': 'B', 'Anna': 'B', 'Bob': 'C', 'David': 'A', 'Simon': 'C'}

#Removing Items from a Python Dictionary

#To remove an item from a dictionary, we can use the del keyword and the key in square brackets:

grades = {'John': 'B', 'Anna': 'B', 'Bob': 'C', 'David': 'A', 'Simon': 'C'}
del grades['David']   # David was actually taking another class
print(grades)         # {'John': 'B', 'Anna': 'B', 'Bob': 'C', 'Simon': 'C'}
del grades['David']   # KeyError - you are not allowed to items not in the dict

#We can also use the pop() method and the key. 
#This method returns the value of the removed item, 
#which can be useful for printing or performing some operation on a removed item:

grades = {'John': 'B', 'Anna': 'B', 'Bob': 'C', 'David': 'A', 'Simon': 'C'}
grade = grades.pop('David')
print('David had a grade of', grade)  # David had a grade of A
print(grades)                         # {'John': 'B', 'Anna': 'B', 'Bob': 'C', 'Simon': 'C'}
grades.pop('David')                   # KeyError

#Iterating over a Python Dictionary

#There are 3 methods that are very useful when iterating over dictionaries:

#keys() — Returns all the keys in the dictionary (names in our example)

grades = {'John': 'B', 'Anna': 'B', 'Bob': 'C', 'David': 'A', 'Simon': 'C'}
for name in grades.keys():
    print(name, '-->', grades[name])
# John --> B
# Anna --> B
# Bob --> C
# David --> A
# Simon --> C

#values() — Returns all the values in the dictionary (grades in our case)

#items() — Returns a list of (key, value) tuples (name & grade together)

grades = {'John': 'B', 'Anna': 'B', 'Bob': 'C', 'David': 'A', 'Simon': 'C'}
for name, grade in grades.items():
    print(name, '-->', grade)
# John --> B
# Anna --> B
# Bob --> C
# David --> A
# Simon --> C