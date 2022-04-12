class Fish:
    
    name = ""
    position = 0
    #status 0 = caught, 1 = free, 2 = saved
    state = 1
    
    def __init__ (self, name, position):
        self.name = name
        self.position = position
        
    def catch (self):
        self.state = 0
        
    def free (self):
        self.state = 1
        
    def save (self):
        self.state = 2
    
    def move(self, amount):
        self.position += amount
        
    def to_string (self):
        my_state = "free"
        if (self.state == 0):
            my_state = "caught"
        elif (self.state == 2):
            my_state = "saved"
        return f"**************\nname:{self.name}\n"\
                f"At position: {self.position}\n"\
                f"State:{my_state}"
        