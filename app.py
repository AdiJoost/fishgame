from board import Board
import csv
import os


def write_to_csv (my_board, amount_of_fish,start_position,save_position,amount_of_fisher,
                  hard_mode):
    #path to csv-file
    file_path = my_path + f"{amount_of_fish}{start_position}{save_position}"\
           f"{amount_of_fisher}{int(hard_mode)}" + ".csv" 
           
    #if file doesn't exist, create it and write headers
    if not (os.path.isfile(file_path)):
        with open (file_path, "a", encoding="UTF-8", newline='') as f:
    
            writer = csv.writer(f)
            writer.writerow(header)
            print("Row written")
    
    #opens csv and writes results on it
    with open (file_path, "a", encoding="UTF-8", newline='') as f:
    
        writer = csv.writer(f)
        writer.writerow(my_board.get_state())
        print("Row written")

my_values = {
                "amount_of_fish": 4,
                "start_position": 8,
                "save_position": 10,
                "amount_of_fisher": 2,
                "hard_mode":False
    }

my_path = "games_played/"
header = ("all_fish", "boat_position","caught_fish", "free_fish", "saved_fish")



my_board = Board(**my_values)
    
my_board.start_game()
print(my_board.get_state())

write_to_csv(my_board, **my_values)

