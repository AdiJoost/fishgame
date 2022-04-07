import fish
import dice

class Board():
    all_fish = []
    start_position = 1
    save_position = 10
    game_dice = -1
    
    def __init__ (self, amount_of_fish, start_position, save_position,\
                  amount_of_fisher):
        self.start_position = start_position
        self.save_position = save_position
        self.game_dice = dice.Dice(amount_of_fish, amount_of_fisher)
        
    def roll_dice(self):
        print(self.game_dice.roll())
    
    def to_string(self):
        return f"***BOARD***\n"\
                f"Amount of fish: {len(self.all_fish)}\n"\
                f"start_position: {self.start_position}\n"\
                f"save_position: {self.save_position}"
    
    def end_game(self):
        pass
    
    
    
board = Board(6,5,10,2)

for i in range (5):
    board.roll_dice()
    
print(board.to_string())