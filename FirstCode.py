blocked_users = {'X', 'Y', 'Z'}
avg_users = {'Ω','β'}
user = input("Enter username: ").capitalize()

if user in blocked_users:
    print(f'{user} is currently restricted. If you wish to request access, please respond.')
    answer = int(input("How many deadly sins exist?: "))
    if answer == 7:
        avg_users.add(user)
        print("Correct")
        print(f"{user} Your access has been successfully restored.")
        print(avg_users)
    else:
        print("Wrong")
        print(f'Unfortunately, {user} has not yet had their access restored.')
elif user in avg_users: 
    print('Welcome back!')
else:
    print (f'{user} Welcome!')
    choice = input("Would you prefer to have this user added to the blocked/average users? Respond with 'blocked' or 'average': ")
    if choice == "blocked":
        print(f'{user} Has been successfully added to blocked users')
        blocked_users.add(user)
        print(blocked_users)
    elif choice == "average":
        print(f'{user} Has been successfully added to average users')
        avg_users.add(user)
        print(avg_users)

