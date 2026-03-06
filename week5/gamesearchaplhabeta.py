import math

# Create empty board
board = [" " for _ in range(9)]

# Print board
def print_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()


# Check winner
def check_winner(b):
    win_conditions = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]

    for cond in win_conditions:
        if b[cond[0]] == b[cond[1]] == b[cond[2]] and b[cond[0]] != " ":
            return b[cond[0]]

    if " " not in b:
        return "Draw"

    return None


# Minimax with Alpha-Beta Pruning
def minimax(b, is_maximizing, alpha, beta):

    result = check_winner(b)

    if result == "X":
        return 1
    elif result == "O":
        return -1
    elif result == "Draw":
        return 0

    # AI turn (maximize)
    if is_maximizing:

        best_score = -math.inf

        for i in range(9):
            if b[i] == " ":
                b[i] = "X"

                score = minimax(b, False, alpha, beta)

                b[i] = " "

                best_score = max(score, best_score)

                alpha = max(alpha, best_score)

                if beta <= alpha:
                    break

        return best_score

    # Player turn (minimize)
    else:

        best_score = math.inf

        for i in range(9):
            if b[i] == " ":
                b[i] = "O"

                score = minimax(b, True, alpha, beta)

                b[i] = " "

                best_score = min(score, best_score)

                beta = min(beta, best_score)

                if beta <= alpha:
                    break

        return best_score


# Find best AI move
def ai_move():

    best_score = -math.inf
    move = -1

    for i in range(9):

        if board[i] == " ":

            board[i] = "X"

            score = minimax(board, False, -math.inf, math.inf)

            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    board[move] = "X"


# Player move
def player_move():

    while True:

        move = int(input("Enter position (1-9): ")) - 1

        if move >= 0 and move < 9 and board[move] == " ":
            board[move] = "O"
            break

        else:
            print("Invalid move. Try again.")


# Game loop
def play_game():

    print("You are O, AI is X")
    print("Board positions:")

    print("1 | 2 | 3")
    print("--+---+--")
    print("4 | 5 | 6")
    print("--+---+--")
    print("7 | 8 | 9")

    while True:

        print_board()

        player_move()

        result = check_winner(board)

        if result:
            print_board()
            print("Result:", result)
            break

        print("AI is thinking...")

        ai_move()

        result = check_winner(board)

        if result:
            print_board()
            print("Result:", result)
            break


# Start the game
play_game()