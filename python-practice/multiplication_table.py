def valid_input(prompt):

    while True:
        try:
            num = int(input(prompt))
            return num
        except ValueError:
            print("Invalid input! Please enter valid number.")

def generate_multiplication_table(num):
    for i in range(1,11):
        print(f"{num} * {i}","=",num * i)    

num = valid_input("Please enter a number for multiplication table: ")
generate_multiplication_table(num)
