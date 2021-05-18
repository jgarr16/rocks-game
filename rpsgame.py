import random

winner = None



def main():
    """docstring"""
    show_header()
    player = "John"
    ai = "Borg"
    play_game(player, ai)


def show_header():
    """docstring"""
    print('------------------------')
    print('  Rock Paper Scissors v1')
    print('------------------------')


def play_game(player_1, player_2):
    """docstring"""
    rounds = 3
    wins_p1 = 0
    wins_p2 = 0

    rolls = ["rock", "paper", "scissors"]

    while wins_p1 < rounds and wins_p2 < rounds:
        roll1 = get_roll(player_1, rolls)
        roll2 = random.choice(rolls)

        losplay, winner, winplay = check_for_winning_throw(player_1, player_2, roll1, roll2, rolls)

        if winner is None:
            print(f"Nobody won, the play was a tie.")
        elif winner == "foul1":
            print(f"{player_1}'s roll was invalid.")
        elif winner == "foul2":
            print(f"{player_2}'s roll was invalid.")
        else:
            if winner == player_1:
                wins_p1 += 1
            if winner == player_2:
                wins_p2 += 1
            print(f"{winplay.title()} beats {losplay}; {winner} wins the play!")
            print(f'Score is {player_1}: {wins_p1} and {player_2}: {wins_p2}')

    overall_winner = None
    if wins_p1 >= rounds:
        overall_winner = player_1
    if wins_p2 >= rounds:
        overall_winner = player_2

    print(f'{overall_winner} wins the game!')
    print()



def check_for_winning_throw(player_1, player_2, roll1, roll2, rolls):
    # Test for a winner
    losplay = None
    winplay = None
    if roll1 == roll2:
        winner = None
    elif roll1 == "foul":
        winner = "foul1"
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
    return losplay, winner, winplay


def get_roll(player_name, rolls):
    """`get-roll` gets the call from Player1 for the current play and validates it."""
    roll = input(f'{player_name}, what is your roll? [rock, paper, scissors]: ')
    roll = roll.lower().strip()
    if roll not in rolls:
        roll = "foul"
    return roll


if __name__ == '__main__':
    main()
