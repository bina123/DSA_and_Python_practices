def validate_password(password):
    if len(password) < 8:
        return False
    
    has_number = False
    for char in password:
        if char.isdigit():
            has_number = True
            break
        
    has_upper = False
    for char in password:
        if char.isupper():
            has_upper = True
            break
        
    return has_number and has_upper
        
def input_validate(promt):
    while True:
        try:
            password = input(promt)
            if(validate_password(password)):
                print("Valid password")
                break
            else:
                print("Invalid Password.  Need 8+ chars, 1 number, 1 uppercase")
        except ValueError:
            print("Password is not valid! It must contain 8 character, a number and uppercase letter")
            
            
password = input_validate("Please enter a valid password which contains 8 character, number and uppercase: ")