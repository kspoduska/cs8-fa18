#!/usr/bin/python3

def main():
    f = open('names.txt')
    
    print('---- Calling find_my_name ----')
    find_my_name(f)
    print('---- find_my_name finished ----')
    
    print('---- Calling appeared_first_in ----')
    print('Jessica first appeared in', appeared_first_in(f, 'Jessica'))
    print('Kharmen first appeared in', appeared_first_in(f, 'Kharmen'))
    print('Orchid first appeared in', appeared_first_in(f, 'Orchid'))
    print('C3P0 first appeared in', appeared_first_in(f, 'C3P0'))
    print('---- appeared_first_in finished ----')
    
    print('---- Calling get_summary_for_name ----')
    print(get_summary_for_name(f, 'Aragorn'))
    print(get_summary_for_name(f, 'Legolas'))
    print(get_summary_for_name(f, 'Leia'))
    print(get_summary_for_name(f, 'Kelly'))
    print('---- get_summary_for_name finished ----')


def find_my_name(f):
    """Seek to the beginning of f, loop through each of its lines and
       print the line if it contains your name."""
    f.seek(0)
    for l in f:
        if ',Jason,' in l:
            print(l, end='')  # l already contains a new line


def appeared_first_in(f, search_for):
    f.seek(0)
    for l in f:
        if ',{},'.format(search_for) in l:
            return l[:4]
    return -1
    
    
def get_summary_for_name(f, search_for):
    f.seek(0)
    first_year = 0
    count = 0
    total = 0
    for l in f:
        items = l.rstrip().split(',')
        if search_for == items[1]:
            if not first_year:
                first_year = items[0]
            count += 1
            total += int(items[3])
            
    return '{}: appears in {} years, first in {}, {:,} total babies'.format(
            search_for, count, first_year, total
        )

main()