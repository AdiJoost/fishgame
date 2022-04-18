from board import Board
import csv

amount_of_fish = 4
start_position = 5
save_position = 10
amount_of_fisher = 2
hard_mode = False
my_path = "games_played/"
header = ("all_fish", "boat_position","caught_fish", "free_fish", "saved_fish")



my_board = Board(amount_of_fish=amount_of_fish,
                 start_position=start_position,
                 save_position=save_position,
                 amount_of_fisher=amount_of_fisher)
    
my_board.start_game()
print(my_board.get_state())

with open (my_path + f"{amount_of_fish}{start_position}{save_position}"\
           f"{amount_of_fisher}{int(hard_mode)}", "a", encoding="UTF-8", newline='') as f:
    
    writer = csv.writer(f)
    writer.writerow(my_board.get_state())
    print("Row written")