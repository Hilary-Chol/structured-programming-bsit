def area(length, width):
    print(f'Area: {length * width}')

def perimeter(length, width):
    print(f'Perimeter: {2 * (length + width)}')

rectangle_length = int(input('Enter length: '))
rectanle_width = int(input('Enter width: '))

area(rectangle_length, rectanle_width)
perimeter(rectangle_length, rectanle_width)