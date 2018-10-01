#!/usr/bin/python3
import random

def main():
    # Basic game board initialization.
    game_board = [
        ['', '', ''],
        ['', '', ''],
        ['', '', '']
    ]
    print('Thanks for playing!')
   
 
def display_board(game_board):
    """This function prints the game board for the user to see its state."""
    pass
                
                
def get_user_move(game_board, symbol):
    """Ask the user for their row and column move and set the game_board with
       their symbol."""
    pass
    
    
def get_computer_move(game_board, symbol):
    """Generate random number coordinates for the computer to place their
    symbol."""
    pass
    

def is_legal_move(game_board, row, col):
    """Check to see if the row and col provided are within the boundaries of 
       the board and if the space is unoccupied."""
    pass
    
def is_draw(game_board):
    """Determine if a game is a draw by checking each space. Once we find at
       least one empty spot, we can return False since it's a playable spot."""
    pass

def has_player_won(game_board, symbol):
    """Check to see if the given symbol has won the game in any of the possible
       ways."""
    
    # Remember, with sequences the multiplication
    # operator repeats the value so 'X' * 3 == 'XXX'
    winner_sequence = symbol * 3 
    
    # Check for horizontal wins
    for r in range(len(game_board)):
        row_symbols = ''
        for c in range(len(game_board[r])):
            row_symbols += game_board[r][c]
        if row_symbols == winner_sequence:
            return True
        
    # Check for vertical wins
    for c in range(len(game_board[0])):
        col_symbols = ''
        for r in range(len(game_board)):
            col_symbols += game_board[r][c]
        if col_symbols == winner_sequence:
            return True
            
    # Check for the two diagonal wins
    # Note this will only work on a square board!
    diag_symbols = ''
    anti_diag_symbols = ''
    for rc in range(len(game_board)):
        diag_symbols += game_board[rc][rc]
        anti_diag_symbols += game_board[rc][len(game_board) - 1 - rc]
    if winner_sequence in (diag_symbols, anti_diag_symbols):
        return True
    
    # If we got here, nobody won yet
    return False
    
main()
