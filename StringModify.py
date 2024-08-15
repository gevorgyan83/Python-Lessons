## 5 MOST USEFULL STRING MODIFYING METHODS IN PYTHON

#.replace(): Replaces a substring with another.

text = "hello world"
new_text = text.replace("world", "Python")
print(new_text)  # Output: "hello Python"

#.strip(): Removes leading and trailing whitespace.

text = "   hello world   "
print(text.strip())  # Output: "hello world"

#.lstrip(): Removes leading whitespace.

text = "   hello world"
print(text.lstrip())  # Output: "hello world"

#.rstrip(): Removes trailing whitespace.

text = "hello world   "
print(text.rstrip())  # Output: "hello world"

#.zfill(): Pads the string on the left with zeros to fill the width.

text = "42"
print(text.zfill(5))  # Output: "00042"


## SPLITTING AND JOINING STRINGS IN PYTHON

#Splitting: The .split() method divides a string into a list, based on a delimiter.

text = "apple,banana,cherry"
words = text.split(",")  # Splits the string at each comma
print(words)  # Output: ['apple', 'banana', 'cherry']

#Joining: The .join() method combines a list of strings into a single string, with an optional separator.

words = ['apple', 'banana', 'cherry']
text = ", ".join(words)  # Joins the list elements with a comma and space
print(text)  # Output: "apple, banana, cherry" 