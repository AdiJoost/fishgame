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
        result = self.game_dice.roll()
        if (result == -1):
            self.boat_position += 1
            if (self.boat_position == self.save_position - 1):
                self.end_game()
        else:
            if (self.all_fish[result].position <= self.boat_position):
                self.all_fish[result].catch()
            else:
                self.all_fish[result].move(1)
                if (self.all_fish[result].position == self.save_position\
                    and self.all_fish[result].state == 1):
                    self.all_fish[result].save()
            
        
    def fill_fish(self, amount_of_fish):
        for i in range (amount_of_fish):
            self.all_fish.append(fish.Fish(f"Fish {i}", self.start_position))
    
    def to_string(self):
        return f"***BOARD***\n"\
                f"Amount of fish: {len(self.all_fish)}\n"\
                f"start_position: {self.start_position}\n"\
                f"save_position: {self.save_position}"
                
    def start_game(self):
        while (self.boat_position < self.save_position):
            self.roll_dice()
        for my_fish in self.all_fish:
            if (my_fish.state != 2):
                my_fish.catch()
        self.end_game() 
                
    
    def end_game(self):
        print(self.get_fish())
    
    def get_fish(self):
        return_value = []
        for my_fish in self.all_fish:
            return_value.append((my_fish.name, my_fish.position, my_fish.state))
        return return_value
        
    def get_state(self):
        pass
    
    
