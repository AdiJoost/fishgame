import csv

def read_file (my_path):
    with open(my_path, "r", encoding="utf-8") as file:
        csv_reader = csv.reader(file)
        headers = next(csv_reader)
    
        data = []
        for row in csv_reader:
            data.append(row)
    return headers, data

def evaluate_catchrate(header, data):
    games_played = len(data)
    amount_of_fish = data[0][0]
    catch_list = {}
    #creates an entry for each possible amount of caught fish (catch_list[i]
    #== i caught fish)
    for i in range(int(amount_of_fish) + 1):
        catch_list[i] = 0
    for row in data:
        catch_list[int(row[2])] += 1
    
    return games_played, amount_of_fish, catch_list

def create_path (head_path, amount_of_fish, start_position,
                 save_position, amount_of_fisher, hard_mode):
    return head_path + f"{amount_of_fish}{start_position}{save_position}"\
           f"{amount_of_fisher}{int(hard_mode)}" + ".csv" 

#
head_path = "games_played/"
amount_of_fish = 4
save_position = 10
amount_of_fisher = 2
hard_mode = False
start_position = 1

my_path = create_path(head_path, amount_of_fish, start_position, save_position, amount_of_fisher, hard_mode)

header, data = read_file(my_path)

games_played, amount_of_fish, catch_list = evaluate_catchrate(header, data)

print(games_played)
print(amount_of_fish)
print(catch_list)