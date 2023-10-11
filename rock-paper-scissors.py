import random

def get_choices():
    player_choice = input("Enter your move (rock. paper, scissors): ")
    moves = ["rock", "paper", "scissors"]
    comp_choice = random.choice(moves)
    choices = {"player" : player_choice, "computer" : comp_choice}
    return choices
    

def check_for_win(player, computer):
    
    print(f"you chose {player} and computer chose {computer}")
    #print("you chose " + player + " and computer chose " + computer)
    
    if player == computer:
        return "its a tie!"
    
    elif player == "rock":
        if computer == "scissors":
            return "you win!"
        else:
            return "computer win!"
    
    elif player == "paper":
        if computer == "scissors":
            return "computer win!"
        else:
            return "you win!"
    
    #and computer == "scissors":
    #   return "you win!"
    #elif computer == "rock" and player == "scissors":
    #   return "computer win!"


choice = get_choices()
print(check_for_win(choice["player"], choice["computer"]))
