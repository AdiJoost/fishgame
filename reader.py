import csv

def read_file (my_path):
    with open(my_path, "r", encoding="utf-8") as file:
        csv_reader = csv.reader(file)
        headers = next(csv_reader)
    
        data = []
        for row in csv_reader:
            data.append(row)
    return headers, data


my_path = "games_played/411020.csv"

header, data = read_file(my_path)

print(header)
for row in data:
    print(row)