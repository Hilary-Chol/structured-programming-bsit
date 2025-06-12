print(" enter number")

grade = None

#the progam below take marks and gives grade according to the mark given
#0-39 F, 40-44 is E-, 45-49 is E, 50-54 is D, 55-59 is D+, 60-64 is C,
#65-69 C+, 70-74 is B, 75-79 is B+, 80-90 is A and 90-100 is A+
def grader():
    mark = int(input())
    if mark >= 0 and mark <= 100:
        if(mark >= 90 and mark <= 100):
            grade = "A+"
            print(f"The grade for the mark {mark} is {grade}")
        elif(mark >= 80 and mark <= 90):
            grade = "A"
            print(f"The grade for the mark {mark} is {grade}")
        elif(mark >= 75 and mark < 80):
            grade = "B+"
            print(f"The grade for the mark {mark} is {grade}")
        elif(mark >= 70 and mark < 75):
            grade = "B"
            print(f"The grade for the mark {mark} is {grade}")
        elif(mark >= 65 and mark < 70):
            grade = "C+"
            print(f"The grade for the mark {mark} is {grade}")
        elif(mark >= 60 and mark < 65 ):
            grade = "C"
            print(f"The grade for the mark {mark} is {grade}")
        elif(mark >= 55 and mark < 60):
            grade = "D+"
            print(f"The grade for the mark {mark} is {grade}")
        elif(mark >= 50 and mark < 55):
            grade = "D"
            print(f"The grade for the mark {mark} is {grade}")
        elif(mark >= 45 and mark < 50):
            grade = "E"
            print(f"The grade for the mark {mark} is {grade}")
        elif(mark >= 40 and mark < 45):
            grade = "E-"
            print(f"The grade for the mark {mark} is {grade}")
        elif(mark >= 0 and mark < 40):
            grade = "F"
            print(f"The grade for the mark {mark} is {grade}")
    else: 
        print("please enter a number between 0 and 100")
        grader()

grader()
