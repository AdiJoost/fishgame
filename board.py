import fish
import dice

class Board():
    """This class is a Board, wich controlls the game played on it
    
    The Board will create a Fisherboat with a specific amount of fisher. It
    will also create all independent fish and holds them in the all_fish-
    variable. The Board will get a dice according to the amount of 
    players in the game. The instance of the class holds:
        
        all_fish (list with all fish)
        start_position (int where fish start)
        save_position (int where fish are safe)
        boat_position (int where the boat is (always 0 at start))
        game_dice (dice-object for board)
        
    Added note: IF the start_position of the fish is equal or bigger
    than the save_position, all fish will be caught, because they never
    reach the save_position itself. (They are already pass)
    """
    
    def __init__ (self, amount_of_fish: int, start_position: int,\
                  save_position: int, amount_of_fisher: int,
                  hard_mode: bool):
        self.start_position = start_position
        self.save_position = save_position
        self.game_dice = dice.Dice(amount_of_fish, amount_of_fisher)
        self.boat_position = 0
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
            
        
    def fill_fish(self, amount_of_fish: int):
        #clear the list of fish, before filling new fish
        self.all_fish = []
        for i in range (amount_of_fish):
            self.all_fish.append(fish.Fish(f"Fish {i}", self.start_position))
    
    def to_string(self) -> str:
        return f"***BOARD***\n"\
                f"Amount of fish: {len(self.all_fish)}\n"\
                f"start_position: {self.start_position}\n"\
                f"save_position: {self.save_position}\n"\
                f"boat_position: {self.boat_position}"
                
    def start_game(self) -> list:
        """This will start the Board an plays the game until the fisher
        have arrived at the save zone. Then the function will evaluate
        the outcome of the game by using self.end_game(). It will
        return the list of all fish that played in the game"""
        while (self.boat_position < self.save_position):
            self.roll_dice()

        return self.end_game() 
                
    
    def end_game(self) -> list:
        for my_fish in self.all_fish:
            if (my_fish.state != 2):
                my_fish.catch()
        return self.get_fish()
    
    def get_fish(self) -> list:
        return_value = []
        for my_fish in self.all_fish:
            return_value.append((my_fish.name, my_fish.position, my_fish.state))
        return return_value
        
    def get_state(self) -> tuple:
        """Returns the state of the game as a tuple: (all_fish, boat_position,
        caught_fish, free_fish, saved_fish.)\n
        If the game has ended, free_fish should always be 0"""
        caught_fish = 0
        saved_fish = 0
        free_fish = 0
        for my_fish in self.all_fish:
            if my_fish.state == 0:
                caught_fish += 1
            elif my_fish.state == 1:
                free_fish += 1
            else:
                saved_fish += 1
        return (len(self.all_fish), self.boat_position, caught_fish,\
                free_fish, saved_fish)
    
    
