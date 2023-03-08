import random as random

def get_choice():
    rps = ["rock", "paper", "scissors"]
    player_choice = input("Pilihan anda ? (rock, paper or scissors) ")
    ai_choice = random.choice(rps)
    response = {"player": player_choice, "ai": ai_choice}
    return response

def check_win(player, ai):
    print(f"you chose {player}, computer chose {ai}")
    if player == ai :
        print("draw")
    elif player == "rock" :
        if ai == "scissors" :
            print("win")
        else:
            print("lose")
    elif player == "paper" :
        if ai == "rock" :
            print("win")
        else:
            print("lose")
    elif player == "scissors" :
        if ai == "paper" :
            print("win")
        else:
            print("lose")
    return[player, ai]

choice = get_choice()
result = check_win(choice["player"], choice["ai"])
print(result)