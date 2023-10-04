import random

class Game(): 
    def roll_dice():
        results = 0
        roll = random.randint(1,6)
        roll2 = random.randint(1,6)
        results = roll + roll2
        return(results)
    
    def challenge_outcome(total, modifier):
        total = total + modifier
        print("The modified total: " + str(total))
        if(total == 2 or total == 3):
            return ("Critical Loss")
        elif(total <= 4 or total <=7):
            return ("Loss")
        elif(total <= 8 or total <=10):
            return("Win")
        elif(total == 11 or total >= 12): 
            return("Critical win")

    def change_stats(result):
        if result == "Critical Loss":
            return -1
        elif result == "Critical win":
            return 1
    