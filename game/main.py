import random

def choose_options():
    options = ("rock", "paper", "scissors")
    user_option = input("Choose rock, paper or scissors: ").lower()
   
    if not user_option in options:
        print("That is not a valid choice, try again!")
        # continue
        return None, None

    computer_option = random.choice(options)
    
    return user_option, computer_option

def check_rules(user_option, computer_option, user_victories, computer_victories):
    
    if user_option == computer_option:
        print(f"It is a tie because the computer chose {computer_option}")
    elif user_option == "rock":
        if computer_option == "scissors":
            print(f"You won because the computer chose {computer_option}")
            user_victories += 1
        else:
            print(f"You lost because the computer chose {computer_option}")
            computer_victories += 1
    elif user_option == "paper":
        if computer_option == "rock":
            print(f"You won because the computer chose {computer_option}")
            user_victories += 1
        else:
            print(f"You lost because the computer chose {computer_option}")
            computer_victories += 1
    elif user_option == "scissors":
        if computer_option == "paper":
            print(f"You won because the computer chose {computer_option}")
            user_victories += 1
        else:
            print(f"You lost because the computer chose {computer_option}")
            computer_victories += 1
    return user_victories, computer_victories


def run_game():
       
    computer_victories = 0
    user_victories = 0
    rounds = 1
    
    while True:
        
        print("-" * 10)
        print("ROUND", rounds)
        print("-" * 10)
        print("Computer victories: ", computer_victories)
        print("User victories: ", user_victories)    
        
        rounds += 1
        
        user_option, computer_option = choose_options()
        user_victories, computer_victories = check_rules(user_option, computer_option, user_victories, computer_victories)
        victories(user_victories, computer_victories)        
       

def victories(user_victories, computer_victories):
    if computer_victories == 2:
        print("THE COMPUTER WON WITH A SCORE OF: ", computer_victories, " ", user_victories)
        exit()
        
    if user_victories == 2:
        print("THE USER WON WITH A SCORE OF: ", user_victories, " ", computer_victories)
        exit()

run_game()
        
    
   