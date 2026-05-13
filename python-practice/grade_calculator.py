def calculate_grade(score):
    if score > 90:
        print("A")
    elif score > 80:
        print("B")
    elif score > 70:
        print("C")
    elif score > 60:
        print("D")
    elif score < 60:
        print("F")

def valid_score(prompt):
    while True:
        try:
            score = float(input(prompt))
            return score
        except ValueError:
            print("Invalid input! Please enter a valid number")
            
score = valid_score("Please enter a score: ")
calculate_grade(score)