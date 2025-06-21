# NAME: Hilary Chol Libo Nyawella
# REG. NO. M25B13/050
# ACC. NO B33493

#CHALLANGE 6: FANCY AVERAGE CALCULATOR
def calculate_average(numbers):
    sum = 0
    for number in numbers:
        sum += number
    average = sum / len(numbers)
    return average

numbers = [12, 8, 16, 4, 20]

average = calculate_average(numbers)
print(f"Average: {average}")
