def get_number(prompt):
    """Get a valid number from user"""
    while True:
        try:
            num = float(input(prompt))  # Use float for decimals
            return num
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def get_operation():
    """Get a valid operation from user"""
    actions = ["sum", "subtract", "multiply", "divide"]
    while True:
        action = input("Please enter an operation (sum, subtract, multiply, divide): ").lower()
        if action in actions:
            return action
        print("Invalid operation! Please choose: sum, subtract, multiply, or divide")

def calculate(num1, num2, action):
    """Perform the calculation"""
    match action:
        case "sum":
            return num1 + num2
        case "subtract":
            return num1 - num2
        case "multiply":
            return num1 * num2
        case "divide":
            if num2 == 0:
                return "Error: Cannot divide by zero"
            return num1 / num2
        case _:
            return "Invalid operation"

# Main program
num1 = get_number("Please enter number 1: ")
num2 = get_number("Please enter number 2: ")
action = get_operation()

result = calculate(num1, num2, action)
print(f"\nResult: {result}")