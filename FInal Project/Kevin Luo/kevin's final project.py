from random import randint

game_board = []

player_one = {
    "name": "Player 1",
    "wins": 0,
}

player_two = {
    "name": "Player 2",
    "wins": 0,
}

colors = {
    "reset": "\033[00m",
    "blue": "\033[94m",
    "cyan": "\033[96m",
}


def build_game_board(board):
    for item in range(5):
        board.append(["O"] * 5)


def show_board(board):
    for row in board:
        print(" ".join(row))


def load_game(board):
    del board[:]
    build_game_board(board)
    show_board(board)
    print(colors['reset'])
    ship_col = randint(1, len(board))
    ship_row = randint(1, len(board[0]))
    return {'ship_col': ship_col, 'ship_row': ship_row}


ship_points = load_game(game_board)


def player_turns(total_turns):
    if total_turns % 2 == 0:
        total_turns += 1
        return player_one

    return player_two


def play_again():
    positive = ["yes"]
    negative = ["no"]

    global ship_points

    while True:
        answer = input("Play again? [Y(es) / N(o)]: ").lower().strip()
        if answer in positive:
            ship_points = load_game(game_board)
            main()
            break

        elif answer in negative:
            print("Thanks for playing!")
            exit()


def input_check(ship_row, ship_col, player, board):
    guess_col = 0
    guess_row = 0
    while True:

        try:
            guess_row = int(input("Guess Row:")) - 1
            guess_col = int(input("Guess Col:")) - 1
        except ValueError:

            print("Enter a number only ")
            continue
        else:

            break
    match = guess_row == ship_row - 1 and guess_col == ship_col - 1
    not_on_game_board = (guess_row < 0 or guess_row > 5) or (
            guess_col < 0 or guess_col > 5)

    if match:
        player["wins"] += 1
        print("Congratulations! You sunk my battleship!")
        print('The current match score is %d : %d (Player1 : Player2)' % (
            player_one["wins"], player_two["wins"]))
        print("Thanks for playing!")
        play_again()

    elif not match:
        if not_on_game_board:
            print(" not on board")

        elif board[guess_row][guess_col] == "X" or board[guess_row][
            guess_col] == "Y":
            print("You guessed that one already.")

        else:
            print("You missed my battleship!")
            if player == player_one:
                board[guess_row][guess_col] = "X"
            else:
                board[guess_row][guess_col] = "Y"

        print(colors['cyan'])
        show_board(game_board)
        print(colors['reset'])

    else:
        return 0


begin = input("Type 'start' to begin: ")

while (begin != str('start')):
    begin = input("Type 'start' to begin: ")


def main():
    for turns in range(100):

        if player_turns(turns) == player_one:
            print(ship_points)
            print("Player One")
            input_check(
                ship_points['ship_row'],
                ship_points['ship_col'],
                player_one, game_board
            )

        elif player_turns(turns) == player_two:
            print("Player Two")
            input_check(
                ship_points['ship_row'],
                ship_points['ship_col'],
                player_two, game_board
            )


if __name__ == "__main__":
    main()
