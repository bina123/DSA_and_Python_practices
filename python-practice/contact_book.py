
contacts = {}

def add_contact(name, phone, email):
    contacts[name] = {'phone': phone,'email': email}

def find_contact(name):
    return contacts.get(name,"Contact not found")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        return f"{name} deleted"
    return "Contact not found"

def list_all_contacts():
    for name, info in contacts.items():
        print(f"{name}")
        print(f" Phone: {info['phone']}")
        print(f" Email: {info['email']}")

def search_by_phone(phone):
    for name, info in contacts.items():
        if info['phone'] == phone:
            return name
    return None

add_contact("Alice", "555-1234", "alice@email.com")
add_contact("Bob", "555-5678", "bob@email.com")
add_contact("Charlie", "555-9012", "charlie@email.com")

print(find_contact("Alice"))
list_all_contacts()
print(search_by_phone("555-5678"))