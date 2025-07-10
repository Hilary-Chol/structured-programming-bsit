def sum_of_even_numbers():
    sum = 0
    if num >= 0:
        for i in range(num):
            i += 1
            if i % 2 == 0:
                print(f'{i}')
                sum += i
        print(f'Sum of even numbers: {sum}')
    else:
        print('please enter a positive number')
        sum_of_even_numbers()

num = int(input('Enter a number: '))
sum_of_even_numbers()