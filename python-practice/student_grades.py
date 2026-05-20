students = {}

def add_student(name,grades):
    students[name] = grades
    
def get_average(student):
    if student not in students:
        return f"{student} not exists"
    avg = sum(students[student]) / len(students[student])
    
    return avg

def get_top_student():
    if not students:
        return None
    
    best_student = None
    best_avg = -1
    
    for name,grade in students.items():
        avg = get_average(name)
        if avg > best_avg:
            best_avg = avg
            best_student = name
            
    return best_student, best_avg

def get_all_averages():
    return {name: get_average(name) for name in students }

# Test it
add_student('Alice', [90, 85, 92])
add_student('Bob', [78, 82, 85])
add_student('Charlie', [95, 98, 93])

print(f"Alice's average: {get_average('Alice')}")
print(f"Top student: {get_top_student()}")
print(f"All averages: {get_all_averages()}")