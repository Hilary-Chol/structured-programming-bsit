# NAME: Hilary Chol Libo Nyawella
# REG. NO. M25B13/050
# ACC. NO B33493

#CHALLANGE 5: STUDENT INFORMATION DISPLAY
def display_student_info(name, age):
    print(f"Student Name: {name}")
    print(f"Student Age: {age}")
    if age < 18:
        print("Status: Minor")
    else:
        print("Status: Adult")

student_name = "Alice"
student_Age = 20
display_student_info(student_name, student_Age)