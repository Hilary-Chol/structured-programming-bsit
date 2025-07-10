def grade():
    num = int(input('enter a number')) 
    mark = num
    if mark >= 0 and mark <= 100:
        if mark > 80:
            print('Grade for the number you entered is A')
        elif mark >= 70 and mark <= 79:
            print('Grade for the number you entered is B')
        elif mark >= 60 and mark <= 69:
            print('Grade for the number you entered is C')
        elif mark >= 50 and mark <= 59:
            print('Grade for the number you entered is D')
        else:
            print('Grade for the number you entered is F')
    else:
        print('enter a number between 0 and 100')
        grade()

grade()