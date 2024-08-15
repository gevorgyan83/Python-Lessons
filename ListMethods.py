## 10 MOST USEFULL LIST METHODS IN PYTHON

#.append(): Adds an item to the end of the list.

numbers = [1, 2, 3]
numbers.append(4)
print(numbers)  # Output: [1, 2, 3, 4]

#.extend(): Adds multiple items to the end of the list.

numbers = [1, 2, 3]
numbers.extend([4, 5, 6])
print(numbers)  # Output: [1, 2, 3, 4, 5, 6]

#.insert(): Inserts an item at a specified position.

numbers = [1, 2, 3]
numbers.insert(1, 1.5)  # Inserts 1.5 at index 1
print(numbers)  # Output: [1, 1.5, 2, 3]

#.remove(): Removes the first occurrence of an item.

numbers = [1, 2, 3, 2]
numbers.remove(2)  # Removes the first occurrence of 2
print(numbers)  # Output: [1, 3, 2]

#.pop(): Removes and returns the last item (or specified index).

numbers = [1, 2, 3]
last_item = numbers.pop()  # Removes and returns the last item
print(last_item)  # Output: 3
print(numbers)  # Output: [1, 2]

#.index(): Returns the index of the first occurrence of an item.

numbers = [1, 2, 3, 2]
index_of_item = numbers.index(2)  # Finds the index of the first occurrence of 2
print(index_of_item)  # Output: 1

#.count(): Returns the number of occurrences of an item.

numbers = [1, 2, 3, 2]
count_of_item = numbers.count(2)  # Counts how many times 2 appears in the list
print(count_of_item)  # Output: 2

#.sort(): Sorts the list in place.

numbers = [3, 1, 2]
numbers.sort()  # Sorts the list in ascending order
print(numbers)  # Output: [1, 2, 3]

#.reverse(): Reverses the order of the list.

numbers = [1, 2, 3]
numbers.reverse()  # Reverses the list
print(numbers)  # Output: [3, 2, 1]

#.clear(): Removes all items from the list.

numbers = [1, 2, 3]
numbers.clear()  # Clears the list
print(numbers)  # Output: []
