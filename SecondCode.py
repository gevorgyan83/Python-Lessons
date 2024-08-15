contacts = {"A":"1"}
contact_names = set("Ishkhan")

def delete_contact(name):
    if name in contact_names:
        del contacts[name]
        contact_names.remove(name)
        print("Contact Name Deleted")
    else:
        print("Contact Name Not Found")

def add_contact(name,phone_number):
    if name in contact_names:
        print(f"{name} Already Exists In Contacts")
    else:
        contacts[name] = phone_number
        contact_names.add(name)
        print(f"{name} Has Been Successfully Added To Contacts")

def view_contacts():
    if not contacts:
        print("No Contact list")
    else:
        print("Contacts list: ")
        for name,phone_number in contacts.items():
            print(f"Name: {name}, Phone Number: {phone_number}")
def main():
    while True:
        print("Contact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Delete Contact")
        print("4. Exit")

        choice = input("Enter Your Choice: ")

        if choice == "1":
            name = input("Enter Contacts Name")
            phone_number = int(input("Enter Contacts Phone Number"))
            add_contact(name,phone_number)
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            delete_contact(name)
        elif choice == "4":
            print("Exiting The Program")
            break
        else:
            print("Please Enter Integer As An Answer")

if __name__ == "__main__":
    main()