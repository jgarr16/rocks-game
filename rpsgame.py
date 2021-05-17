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
    rolls = ["rock", "paper", "scissors"]

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
        print(f"{winplay.title()} beats {losplay}; {winner} wins the play!")


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
