# NAME: Hilary Chol Libo Nyawella
# REG. NO. M25B13/050
#ACC. NO B33493

#CHALLANGE 3: AVERAGE CALCULATOR

def calculate_average(numbers):
    total = 0
    for number in numbers:
        total += number

    average = total / len(numbers)
    return average

def classify_average(average):
    if average >= 90:
        return "A"
    elif average >=  80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    elif average >= 50:
        return "E"
    else:
        return "F"
    

student_scores = [95, 88, 72, 65, 79]
average_score = calculate_average(student_scores)
letter_grade = classify_average(average_score)
print(f"{average_score}")
print(f"{letter_grade}")