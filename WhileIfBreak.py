while True:
    user_input = int(input("Enter A Negative Number To Keep Running The Loop (Positive To Quit)"))
    if user_input > 0:
        print("Exiting The Program")
        break
    elif user_input < 0:
        print ("The Number Is Negative")
