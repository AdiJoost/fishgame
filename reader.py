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
    for i in range(int(amount_of_fish) + 1):
        catch_list[i] = 0
    for row in data:
        catch_list[int(row[2])] += 1
    return games_played, amount_of_fish, catch_list


my_path = "games_played/411020.csv"

header, data = read_file(my_path)

games_played, amount_of_fish, catch_list = evaluate_catchrate(header, data)

print(games_played)
print(amount_of_fish)
print(catch_list)