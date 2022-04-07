import fish
import dice

class Board():
    all_fish = []
    start_position = 1
    save_position = 10
    boat_position = 0
    game_dice = -1
    
    def __init__ (self, amount_of_fish, start_position, save_position,\
                  amount_of_fisher):
        self.start_position = start_position
        self.save_position = save_position
        self.game_dice = dice.Dice(amount_of_fish, amount_of_fisher)
        self.fill_fish(amount_of_fish)
        
    def roll_dice(self):
        print(self.game_dice.roll())
        
    def fill_fish(self, amount_of_fish):
        for i in range (amount_of_fish):
            self.all_fish.append(fish.Fish(f"Fish {i}", self.start_position))
    
    def to_string(self):
        return f"***BOARD***\n"\
                f"Amount of fish: {len(self.all_fish)}\n"\
                f"start_position: {self.start_position}\n"\
                f"save_position: {self.save_position}"
                
    
    def end_game(self):
        pass
    
    
    
board = Board(6,5,10,2)

    
print(board.to_string())

for i in range(len(board.all_fish)):
    print(board.all_fish[i].to_string())