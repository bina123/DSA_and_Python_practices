def format_greeting(name):
    """Takes a name and returns a formatted greeting"""
    name = name.strip().title()
    return f"Hello, {name}! Welcome!"

user_name = input("Please enter your name: ")
greeting = format_greeting(user_name)
print(greeting)