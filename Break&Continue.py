#BREAK & CONTINUE

#The break statement is used to immediately exit a loop, regardless of the loop's condition. 
# When break is encountered, the loop stops executing, and the program continues with the next statement after the loop.

while True:
    n = input('Enter a number or q to quit: ')
    if n == 'q':
        break
    square = int(n) ** 2
    print('Square:', square)

#The continue statement is used to skip the rest of the code inside the loop for the current iteration and proceed 
# to the next iteration of the loop.

for i in range(1, 6):
    if i == 3:
        continue
    print(i)

#The loop prints numbers from 1 to 5, but when i equals 3, the continue statement is triggered, 
# causing the loop to skip printing 3 and move directly to the next iteration.

#Output (1,2,4,5)