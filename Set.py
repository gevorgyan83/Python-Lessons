#Set

#Python sets are a unique collection of elements that are unordered. 
#They are very useful for data manipulation and have many real-world use cases. 
#In this post, we will explore how to create and modify sets in Python, discuss some operations that can be performed on sets, 
#and touch on set comprehension.

#Creating a Set in Python
#To create a set in Python, you can use the built-in set() function or use curly braces {}.

numbers = set()        # Creating an empty set
numbers.add(1)         # {1}
numbers.add(2)         # {1, 2}
numbers.add(3)         # {1, 2, 3}
numbers.add(2)         # {1, 2, 3}

numbers = {1, 2, 3}    # Creating a set with elements

# Use remove() to remove an element from a set
numbers = {1, 2, 3}     # {1, 2, 3}
numbers.remove(2)       # {1, 3}
numbers.remove(2)       # KeyError: 2
numbers.remove(10)      # KeyError: 10

# Use discard() to discard an element from a set
numbers = {1, 2, 3}     # {1, 2, 3}
numbers.discard(2)      # {1, 3}
numbers.discard(2)      # {1, 3} - nothing happened
numbers.discard(10)     # {1, 3} - nothing happened

#Checking if an Element is Present in a Set

blocked_users = {'user1', 'user2'}   # usernames `user1` and `user2` are blocked
user = input()                       # Get the username from the input

# Check if the username is blocked
if user in blocked_users:
    print(f'{user} is blocked!')
else:
    print(f'Welcome, {user}!')

#You can also use the not in keyword to check if an element is not a member of a set:

numbers = {1, 2, 3}     # Define a set of numbers
n = int(input())        # Get the current number from the user

# Check if the number entered is not in the set
if n not in numbers:
    print(f'{n} is not in the set.')
else:
    print(f'{n} is in the set.')