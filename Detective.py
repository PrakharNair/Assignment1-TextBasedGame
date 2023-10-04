
class Detective(): 
    def __init__(self, strength, dex, int):
        self.strength = strength
        self.dex = dex
        self.int = int
        
    def get_stats(self):
        return(self.strength, self.dex, self.int)