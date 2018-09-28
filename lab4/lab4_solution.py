#!/usr/bin/python3

def main():
    print_dotted_line()
    x = get_smallest(100, 85.5, 125)
    print('x={}'.format(x))

    print_dotted_line()    
    y = get_largest(100, 85.5, 125)
    print('y={}'.format(y))

    print_dotted_line()
    if is_evenly_divisible_by(75, 5):
        print('75 is evenly divisible by 5')
    else:
        print('75 is not evenly divisible by 5')

    print_dotted_line()
    if is_evenly_divisible_by(75, 7):
        print('75 is evenly divisible by 7')
    else:
        print('75 is not evenly divisible by 7')


def print_dotted_line():
    print('.' * 80)


def get_smallest(a, b, c):
    smallest = a
    if b < smallest:
      smallest = b
    if c < smallest:
      smallest = c
    return smallest


def get_largest(a, b, c):
    largest = a
    if b > largest:
      largest = b
    if c > largest:
      largest = c
    return largest


def is_evenly_divisible_by(x, y):
    return x % y == 0

main()	
