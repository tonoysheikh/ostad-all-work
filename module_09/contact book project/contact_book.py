# 1. create contact
# 2. view all contacts
# 3. search contact
# 4. remove contact
# 5. update contact
# 6. exit

contact_book = [
    {
        "Name": "Tonoy",
        "Contact_number": "2102023012",
        "Email": "salmanjohirtonoy17@gmail.com",
    },
    {
        "Name": "Tonoy1",
        "Contact_number": "2102023011",
        "Email": "tonoy17@gmail.com",
    },
    {
        "Name": "Tonoy2",
        "Contact_number": "2102023010",
        "Email": "salmanjohirtonoy17@gmail.com",
    }
]

# contact_book = []

def create_contact():
    Name = input("Name: ")
    Contact_number = input("Contact Number: ")
    Email = input("Email: ")
    
    contact_data = {
        "Name": Name,
        "Contact_number": Contact_number,
        "Email": Email,
    }
    
    contact_book.append(contact_data)
    print("Contact successfully created.")

def view_all_contacts():
    for contact in contact_book:
        print(f"Name: {contact['Name']}\nContact Number: {contact['Contact_number']}\nEmail: {contact['Email']}\n")

def search_contact():
    search_name = input("Enter name to search: ")
    found = False
    for contact in contact_book:
        if search_name.lower() in contact["Name"].lower():
            print(contact["Name"], contact["Contact_number"], contact["Email"], sep=" | ")
            found = True
    if not found:
        print("Contact not found.")

def remove_contact():
    remove_name = input("Enter name to remove: ")
    found = False
    for index, contact in enumerate(contact_book):
        if remove_name.lower() in contact["Name"].lower():
            print(f"{index + 1}. {contact['Name']}, {contact['Contact_number']}, {contact['Email']}")
            found = True
    if not found:
        print("Contact not found.")
        return
    remove_index = int(input("Enter index to remove: ")) - 1
    if 0 <= remove_index < len(contact_book):
        contact_book.pop(remove_index)
        print("Contact successfully removed.")
    else:
        print("Invalid index.")

def update_contact():
    update_name = input("Enter name to update: ")
    found = False
    for index, contact in enumerate(contact_book):
        if update_name.lower() in contact["Name"].lower():
            print(f"{index + 1}. Name : {contact['Name']}, {contact['Contact_number']}, {contact['Email']}")
            found = True
    if not found:
        print("Contact not found.")
        return
    update_index = int(input("Enter index to remove: "))-1
    
    new_name = input("New name :")
    new_contact = input("New contact Number :")
    new_email = input("New email address :")
    
    contact_book[update_index].update({
        "Name": new_name,
        "Contact_number": new_contact,
        "Email": new_email
    })
    print("Successfully updated")

while True:
    menu = """
    1. Create a new contact
    2. View all contacts
    3. Search a contact
    4. Remove a contact
    5. Update a contact
    6. Exit
    """
    print(menu)
    
    choice = int(input("Enter your choice: "))
    if choice == 1:
        create_contact()
    elif choice == 2:
        view_all_contacts()
    elif choice == 3:
        search_contact()
    elif choice == 4:
        remove_contact()
    elif choice == 5:
        update_contact()
    elif choice == 6:
        exit()
    else:
        print("Invalid choice. Please try again.")
