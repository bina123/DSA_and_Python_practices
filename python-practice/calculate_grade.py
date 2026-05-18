def calculate_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'
    
def calculate_gpa(grades):
    grade_points = {'A':4,'B':3,'C':2,'D':1,'F':0}
    total = sum(grade_points[grade] for grade in grades)
    return total / len(grades)

scores = [95, 87, 76, 82, 91]
letter_grades = [calculate_grade(s) for s in scores]
print(letter_grades)  
print(f"GPA: {calculate_gpa(letter_grades):.2f}")  # GPA: 3.40