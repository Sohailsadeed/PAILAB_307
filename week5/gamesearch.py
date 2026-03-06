import math

# Initialize board
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
        [0,1,2],[3,4,5],[6,7,8],  # rows
        [0,3,6],[1,4,7],[2,5,8],  # columns
        [0,4,8],[2,4,6]           # diagonals
    ]

    for cond in win_conditions:
        if b[cond[0]] == b[cond[1]] == b[cond[2]] and b[cond[0]] != " ":
            return b[cond[0]]

    if " " not in b:
        return "Draw"

    return None


# Minimax algorithm
def minimax(b, is_maximizing):

    result = check_winner(b)

    if result == "X":
        return 1
    elif result == "O":
        return -1
    elif result == "Draw":
        return 0

    if is_maximizing:
        best_score = -math.inf

        for i in range(9):
            if b[i] == " ":
                b[i] = "X"
                score = minimax(b, False)
                b[i] = " "
                best_score = max(score, best_score)

        return best_score

    else:
        best_score = math.inf

        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                score = minimax(b, True)
                b[i] = " "
                best_score = min(score, best_score)

        return best_score


# Find best move for AI
def ai_move():
    best_score = -math.inf
    move = -1

    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            score = minimax(board, False)
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
            print("Invalid move, try again.")


# Game loop
def play_game():
    print("You are O, AI is X")
    print("Positions are numbered 1-9")
    print("")

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


# Start game
play_game()