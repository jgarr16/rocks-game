
print('------------------------')
print('  Rock Paper Scissors v1')
print('------------------------')

player_1 = "John" # input("Enter player 1's name: ")
player_2 = "Kyong" # input("Enter player 2's name: ")

rolls = ["rock","paper","scissors"]

roll1 = input(f'{player_1}, what is your roll? [rock, paper, scissors]: ').strip()
if roll1 not in rolls:
    print(f"Sorry {player_1}, {roll1} is not a valid choice.")
roll2 = input(f'{player_2}, what is your roll? [rock, paper, scissors]: ').strip()
if roll2 not in rolls:
    print(f"Sorry {player_2}, {roll2} is not a valid choice.")

if roll1.lower() == rolls[0]:
    if roll2.lower() == rolls[0]:
        print(f"It's a tie, try again.")
    elif roll2.lower() == rolls[1]:
        print(f"{player_2}'s {roll2.lower()} beats {player_1}'s {roll1.lower()}.")
    else:
        print(f"{player_1}'s {roll1.lower()} beats {player_2}'s {roll2.lower()}.")
if roll1.lower() == rolls[1]:
    if roll2.lower() == rolls[1]:
        print(f"It's a tie, try again.")
    elif roll2.lower() == rolls[2]:
        print(f"{player_2}'s {roll2.lower()} beats {player_1}'s {roll1.lower()}.")
    else:
        print(f"{player_1}'s {roll1.lower()} beats {player_2}'s {roll2.lower()}.")
if roll1.lower() == rolls[2]:
    if roll2.lower() == rolls[2]:
        print(f"It's a tie, try again.")
    elif roll2.lower() == rolls[0]:
        print(f"{player_2}'s {roll2.lower()} beats {player_1}'s {roll1.lower()}.")
    else:
        print(f"{player_1}'s {roll1.lower()} beats {player_2}'s {roll2.lower()}.")