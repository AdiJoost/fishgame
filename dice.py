from random import randint

class Dice():
    total_sites = 6
    sites_for_fisher = 2
    def __init__ (self, amount_of_fish: int, amount_of_fisher: int):
        self.total_sites = amount_of_fish + amount_of_fisher
        self.sites_for_fisher = amount_of_fisher
    
    def roll(self) -> int:
        #rolls a dice and returns the number. If the number of the result 
        #is a fisher, it will return -1
        result = randint(0, self.total_sites - 1) - self.sites_for_fisher
        if result < 0:
            return -1
        else:
            return result
        