import string


# noinspection SpellCheckingInspection
def tictactoe_printer(cells):
    print("-" * 9 + "\n|", cells[0], cells[1], cells[2], "|" + "\n|", cells[3], cells[4], cells[5], "|"
          + "\n|", cells[6], cells[7], cells[8], "|\n" + "-" * 9)


print("Tic-Tac-Toe!")
game_state = list("_" * 9)
game_state_matrix = [game_state[:3], game_state[3:6], game_state[6:9]]
tictactoe_printer([x if x in ("X", "O") else " " for x in game_state])
counter = 0
winner = ""

while True:
    while True:
        x, y = input("Enter the coordinates: ").split()
        if x in string.digits and y in string.digits:
            if int(x) in range(1, 4) and int(y) in range(1, 4):
                row = int(x) - 1
                column = int(y) - 1
                if game_state_matrix[row][column] == "_":
                    break
                else:
                    print("This cell is occupied! Choose another one!")
            else:
                print("Coordinates should be from 1 to 3!")
        else:
            print("You should enter numbers!")

    counter += 1
    if counter % 2 == 1:
        game_state_matrix[row][column] = "X"
    else:
        game_state_matrix[row][column] = "O"

    game_state = [x for lst in game_state_matrix for x in lst]
    winning_combinations = [game_state[:3], game_state[3:6], game_state[6:9],
                            [game_state[0], game_state[3], game_state[6]],
                            [game_state[1], game_state[4], game_state[7]],
                            [game_state[2], game_state[5], game_state[8]],
                            [game_state[0], game_state[4], game_state[8]],
                            [game_state[2], game_state[4], game_state[6]]]
    tictactoe_printer([x if x in ("X", "O") else " " for x in game_state])

    if ["X", "X", "X"] in winning_combinations:
        winner = "X wins"
        break
    elif ["O", "O", "O"] in winning_combinations:
        winner = "O wins"
        break
    elif "_" not in game_state:
        winner = "Draw"
        break

print(winner)
