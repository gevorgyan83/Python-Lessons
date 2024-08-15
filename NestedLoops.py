#Nested Loops

#Nested loops in Python allow you to loop through multiple sequences at the same time. 
#They are useful for iterating through multi-dimensional data structures,
# such as lists of lists, matrices, and other complex data structures.

lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for sublist in lists:
    for item in sublist:
        print(item)

#_______________________________________________________________________________________
#This code will output all the items in the list one by one — 1, 2, 3, 4, 5, 6, 7, 8, 9.
#_______________________________________________________________________________________

#You can also use nested loops to iterate through a matrix (2D list), using indices:

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=' ')
    print()