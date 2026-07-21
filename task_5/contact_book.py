list_of_dict = []

def main():
    while True:
        print("What the next action choo a number between 1 and 5")
        print("1 to add to the contact list" \
        "\n2 to search a person by name" \
        "\n3 to delete a contact" \
        "\n4 to view available contacts\n" \
        "5 to exit")
        action = int(input())
        if action == 1:
            add_contact()
        elif action == 2:
            name = input("name of contact to search: ")
            details = search_contact(name)
            print(details)
        elif action == 3:
            name = input("name of contact to delete: ")
            delete_contact(name)
        elif action == 4:
            view_all()
        elif action == 5:
            break
        else:
            print("Invalid number choose between 1 and 5")


def add_contact():
    name = input("Name: ")
    phone_number = int(input("Phone number: "))
    email = input("Email: ")
    new_dict = {"Name": name, "Phone": phone_number, "email": email}
    list_of_dict.append(new_dict)
    print(f"Contact {name} added")
    return

def search_contact(name):
    for dict in list_of_dict:
        if name == dict['Name']:
            return dict
    return None

def delete_contact(name):
    for dict in list_of_dict:
        if name == dict['Name']:
            list_of_dict.remove(dict)
            return

def view_all():
    print(f"Name\tPhone Number\tEmail")
    for dict in list_of_dict:
        print(f"{dict['Name']}\t{dict['Phone']}\t{dict['email']}")
    print()
    return


if __name__ == "__main__": main()