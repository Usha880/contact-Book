# Contact book data structure
contacts = []

# Function to add a new contact
def add_contact():
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email address (optional): ")
    address = input("Enter the contact's address (optional): ")
    contact = {"name": name, "phone": phone, "email": email, "address": address}
    contacts.append(contact)
    print("Contact added successfully!")

# Function to display all contacts with name and phone numbers
def display_contacts():
    print("Name\t\tPhone")
    print("-------------------")
    for contact in contacts:
        print(f"{contact['name']}\t{contact['phone']}")

# Function to search for a contact by name
def search_contact(name):
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print("\nContact found:")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
            return
    print("Contact not found.")

# Function to update a contact
def update_contact():
    name = input("Enter the name of the contact you want to update: ")
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contact["phone"] = input("Enter the updated phone number: ")
            contact["email"] = input("Enter the updated email address (optional): ")
            contact["address"] = input("Enter the updated address (optional): ")
            print("Contact updated successfully!")
            return
    print("Contact not found.")

# Function to delete a contact
def delete_contact():
    name = input("Enter the name of the contact you want to delete: ")
    for i, contact in enumerate(contacts):
        if contact["name"].lower() == name.lower():
            del contacts[i]
            print("Contact deleted successfully!")
            return
    print("Contact not found.")

# Example usage
while True:
    print("\nContact Book")
    print("1. Add Contact")
    print("2. Display Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_contact()
    elif choice == 2:
        display_contacts()
    elif choice == 3:
        name = input("Enter the name of the contact you want to search for: ")
        search_contact(name)
    elif choice == 4:
        update_contact()
    elif choice == 5:
        delete_contact()
    elif choice == 6:
        break
    else:
        print("Invalid choice. Please try again.")