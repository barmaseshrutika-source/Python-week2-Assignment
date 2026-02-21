
contacts = {}

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    contacts[name] = phone
    print("Contact Added Successfully!\n")

def search_contact():
    name = input("Enter Name to Search: ")
    if name in contacts:
        print("Phone:", contacts[name])
    else:
        print("Contact Not Found!\n")

def update_contact():
    name = input("Enter Name to Update: ")
    if name in contacts:
        phone = input("Enter New Phone: ")
        contacts[name] = phone
        print("Contact Updated!\n")
    else:
        print("Contact Not Found!\n")

def delete_contact():
    name = input("Enter Name to Delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact Deleted!\n")
    else:
        print("Contact Not Found!\n")

while True:
    print("1.Add 2.Search 3.Update 4.Delete 5.Exit")
    choice = input("Choose Option: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        update_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        break
    else:
        print("Invalid Choice\n")