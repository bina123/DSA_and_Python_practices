import pandas as pd

students = pd.DataFrame({
    'student_id' : [1,2,3,4],
    'name': ['Alice','Bob','Charlie','David'],
    'course_id': [101,102,101,103]
})

courses = pd.DataFrame({
    'course_id' : [101,102,104],
    'course_name' : ['Math','English','Science']
})

result1 = pd.merge(students,courses,on="course_id",how="inner")
print(result1)

result2 = pd.merge(students,courses,on="course_id",how="left")
print(result2)

students_without_course = result2["course_name"].isna().sum()
print(f"\nStudents without course: {students_without_course}")

# Task 4: Show all students WITH a course
students_with_course = result2[result2["course_name"].notna()]
print(f"\n Students with course: {students_with_course}")


# Task 5: Fill NaN course names with "Not Enrolled"
result_filled = result2.copy()
result_filled["course_name"] = result_filled["course_name"].fillna("Not Enrolled")
print("\nTASK 5 - Filled NaN values:")
print(result_filled)

# Task 6: What percentage of students are enrolled?
enrollement_number = (result2["course_name"].notna().sum()/len(result2)) * 100  
print(f"Enrollment rate: {enrollement_number}%")
