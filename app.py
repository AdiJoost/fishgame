from board import Board

my_board = Board(amount_of_fish=5, start_position=9, save_position=10,\
                 amount_of_fisher=2)
    
print(my_board.start_game())
print(my_board.get_state())