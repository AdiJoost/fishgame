from board import Board
import csv
import os


def write_to_csv (my_board, amount_of_fish,start_position,save_position,
                  amount_of_fisher,
                  hard_mode):
    #path to csv-file
    file_path = my_path + f"{amount_of_fish}{start_position}{save_position}"\
           f"{amount_of_fisher}{int(hard_mode)}" + ".csv" 
           
    #if file doesn't exist, create it and write headers
    if not (os.path.isfile(file_path)):
        with open (file_path, "a", encoding="UTF-8", newline='') as f:
    
            writer = csv.writer(f)
            writer.writerow(header)
            
    
    #opens csv and writes results on it
    with open (file_path, "a", encoding="UTF-8", newline='') as f:
    
        writer = csv.writer(f)
        writer.writerow(my_board.get_state())
        

my_values = {
                "amount_of_fish": 4,
                "start_position": 8,
                "save_position": 10,
                "amount_of_fisher": 2,
                "hard_mode":False
    }

my_path = "games_played/"
header = ("all_fish", "boat_position","caught_fish", "free_fish", "saved_fish")


for i in range(1, 11):
    my_values["start_position"] = i
    for _ in range(10000):
        my_board = Board(**my_values)
        my_board.start_game()
        write_to_csv(my_board, **my_values)
    print("1000 games played")



