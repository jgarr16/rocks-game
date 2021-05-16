import random


print('------------------------')
print('  Rock Paper Scissors v1')
print('------------------------')

player_1 = "You" # input("Enter player 1's name: ")
player_1 = player_1.title().strip()
player_2 = "Borg" # input("Enter player 2's name: ")
player_2 = player_2.title().strip()

rolls = ["rock","paper","scissors"]

roll1 = input(f'{player_1}, what is your roll? [rock, paper, scissors]: ')
roll1 = roll1.lower().strip()
if roll1 not in rolls:
    print(f"Sorry {player_1}, {roll1} is not a valid choice.")
roll2 = random.choice(rolls) # input(f'{player_2}, what is your roll? [rock, paper, scissors]: ')
roll2 = roll2.lower().strip()
if roll2 not in rolls:
    print(f"Sorry {player_2}, {roll2} is not a valid play.")


# Test for a winner
winner = None

if roll1 == roll2:
    winner = None
elif roll1 == rolls[0]:
    if roll2 == rolls[1]:
        winner = player_2
        winplay = roll2
        looser = player_1
        losplay = roll1
    else:
        winner = player_1
        winplay = roll1
        looser = player_2
        losplay = roll2
elif roll1 == rolls[1]:
    if roll2 == rolls[2]:
        winner = player_2
        winplay = roll2
        looser = player_1
        losplay = roll1
    else:
        winner = player_1
        winplay = roll1
        looser = player_2
        losplay = roll2
elif roll1 == rolls[2]:
    if roll2 == rolls[0]:
        winner = player_2
        winplay = roll2
        looser = player_1
        losplay = roll1
    else:
        winner = player_1
        winplay = roll1
        looser = player_2
        losplay = roll2

if winner is None:
    print(f"Nobody won, the play was a tie.")
else:
    print(f"{winplay.title()} beats {losplay}; {winner} wins the play!")