import random
random.seed(1234)

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

def main():
    print("Program starting.")
    print("Welcome to the rock-paper-scissors game!")
    player_name = input("Insert player name: ")
    print(f"Welcome {player_name}!")
    print("Your opponent is RPS-3PO.")
    print("Game starts...\n")
    player_wins = 0
    bot_wins = 0
    ties = 0

    while True:
        print("Options:")
        print("1 - Rock")
        print("2 - Paper")
        print("3 - Scissors")
        print("0 - Quit game")

        player_choice = int(input("Your choice: "))

        if player_choice == 0:
            break

        bot_choice = getBotChoice()

        ascii_art = {1: rock, 2: paper, 3: scissors}
        choices = {1: "rock", 2: "paper", 3: "scissors"}

        print("Rock! Paper! Scissors! Shoot!\n")
        print("#########################")
        print(f"{player_name} chose {choices[player_choice]}.")
        print(f"{ascii_art[player_choice]}")
        print("#########################")
        print(f"RPS-3PO chose {choices[bot_choice]}.")
        print(f"{ascii_art[bot_choice]}")
        print("#########################")

        winner = getWinner(player_choice, player_name, bot_choice)
        if winner == "player":
            player_wins +=1
        elif winner == "bot":
            bot_wins += 1
        else:
            ties += 1
        print()

    print(f"\nResults:")
    print(f"{player_name} - wins ({player_wins}), losses ({bot_wins}), draws ({ties})")
    print(f"RPS-3PO - wins ({bot_wins}), losses ({player_wins}), draws ({ties})")
    print()
    print("Program ending.")
    return None

def getBotChoice():
    return random.randint(1, 3)

def getWinner(player_choice, player_name, bot_choice):
    choices = {1: "rock", 2: "paper", 3: "scissors"}
    if player_choice == bot_choice:
        print(f"\nDraw! Both players chose {choices[player_choice]}.")
        return "draw"
    elif player_choice == 1 and bot_choice == 3:
        print(f"\n{player_name} {choices[player_choice]} beats RPS-3PO {choices[bot_choice]}.")
        return "player"
    elif player_choice == 2 and bot_choice == 1:
        print(f"\n{player_name} {choices[player_choice]} beats RPS-3PO {choices[bot_choice]}.")
        return "player"
    elif player_choice == 3 and bot_choice == 2:
        print(f"\n{player_name} {choices[player_choice]} beats RPS-3PO {choices[bot_choice]}.")
        return "player"
    else:
        print(f"\nRPS-3PO {choices[bot_choice]} beats {player_name} {choices[player_choice]}.")
        return "bot"

main()

