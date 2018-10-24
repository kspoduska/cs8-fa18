#!/usr/bin/python3
import time
import sys

# Multi-line string variable for the main program menu.
MAIN_MENU = (
'''======================================================================
\tEnter 1 to Search for a Movie Title and See its Cast
\tEnter 2 to Search for an Actor/Actress and See their Movies
\tEnter anything else to exit.
======================================================================
Please type an option from the list above:
>>> ''')

# Filename for the IMDB database
IMDB_FILE = 'imdb_data.tsv'

def main():
    """Main program execution function.

    This is already written for you and should not be be modified.
    """
    # Two dict objects will serve as efficient data structures for look ups
    titles_index = {}
    actors_index = {}
    start = time.time()
    rows = build_indexes(titles_index, actors_index)
    print('Indexed {:,} rows from {} in {:,.2f}s'.format(
        rows, IMDB_FILE, time.time() - start))
    memory_used = sys.getsizeof(titles_index) + sys.getsizeof(actors_index)
    print('Using {:,.2f}MB of memory'.format(memory_used / 2 ** 20))

    # Stay in the loop until an invalid action is received.
    while True:
        action = input(MAIN_MENU)
        if action == '1':
            search_for_title(titles_index)
        elif action == '2':
            movies_for_actor(actors_index)
        else:
            print('"{}" is not a valid action. Goodbye!'.format(action))
            break


def build_indexes(titles_index, actors_index):
    """Processes IMDB_FILE and populates two dict data structures.

    Args:
        titles_index: Dict data structure keyed by title values from IMDB_FILE
        actors_index: Dict data structure keyed by actor values from IMDB_FILE
    Returns:
        Number of rows read from IMDB_FILE
    """
    return 0


def sort_by_name(data):
    """Helper function to be passed to the sort() method for titles_index values.

    Args:
        data: dict object
    Return:
        data['name'] Value
    """
    return data['name']


def sort_by_year(data):
    """Helper function to be passed to the sort() method for actors_index values.

    Args:
        data: dict object
    Return:
        data['year'] Value
    """
    return data['year']


def search_for_title(titles_index):
    """Lookup and print the actors/actresses from a movie by title.

    Args:
        titles_index: Dict data structure keyed by title
    """
    print('Not implemented yet')


def movies_for_actor(actors_index):
    """Lookup and print the movies that an actor/actress starred in.

    Args:
        actors_index: Dict data structure keyed by year
    """
    print('Not implemented yet')


main()
