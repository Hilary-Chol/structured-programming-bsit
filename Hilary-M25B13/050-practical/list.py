numbers = []

#The function below loops 5 times 
#to capture 5 numbers and adds them to a list
#instead of writing multiple input functions
def loop(numbers):
    print('Enter 5 numbers: ')
    for i in range(5):
        numbers.append(int(input()))
    print(f'Numbers: {numbers}')

loop(numbers)

def maximum(numbers):
    maximum_number = numbers[0] # is to compare with the value of other objects in the list
    for i in range(len(numbers)):
        if numbers[i] > maximum_number:
            maximum_number = numbers[i]
    print(f'Maximun: {maximum_number}')


def minimum(numbers):
    minimum_number = numbers[0] # is to compare with the value of other objects in the list
    for i in range(len(numbers)):
        if numbers[i] < minimum_number:
            minimum_number = numbers[i]
    print(f'Minimun: {minimum_number}')

def average(numbers):
    sum = 0 # Holds the sum of all the numbers in the list
    for i in range(len(numbers)):
        sum += numbers[i]
    average_value = sum / len(numbers)
    print(f'Average: {average_value}')

maximum(numbers)
minimum(numbers)
average(numbers)
print(f'Sorted: {sorted(numbers)}')