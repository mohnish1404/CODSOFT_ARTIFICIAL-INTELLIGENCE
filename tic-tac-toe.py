import math

# Constants
PLAYER_X = "X"
PLAYER_O = "O"
EMPTY = " "

# Function to check the winner
def check_winner(board):
    # Check rows, columns, and diagonals for a winner
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:  # Check row
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:  # Check column
            return board[0][i]
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:

        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]

    return None  # No winner yet

# Function to check if the board is full
def is_full(board):
    for row in board:
        if EMPTY in row:
            return False
    return True

# Minimax function with Alpha-Beta Pruning
def minimax(board, depth, alpha, beta, is_maximizing):
    winner = check_winner(board)
    if winner == PLAYER_X:
        return 1  # AI wins
    if winner == PLAYER_O:
        return -1  # Human wins
    if is_full(board):
        return 0  # Draw

    if is_maximizing:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_X
                    eval = minimax(board, depth + 1, alpha, beta, False)
                    board[i][j] = EMPTY
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_O
                    eval = minimax(board, depth + 1, alpha, beta, True)
                    board[i][j] = EMPTY
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

# Function to find the best move for the AI (Maximizing Player)
def best_move(board):
    best_val = -math.inf
    move = (-1, -1)
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = PLAYER_X
                move_val = minimax(board, 0, -math.inf, math.inf, False)
                board[i][j] = EMPTY
                if move_val > best_val:
                    best_val = move_val
                    move = (i, j)
    
    return move

# Function to display the board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Function to play the game
def play_game():
    board = [[EMPTY] * 3 for _ in range(3)]
    while True:
        print_board(board)
        
        # Human move (Player O)
        row, col = map(int, input("Enter your move (row col): ").split())
        if board[row][col] == EMPTY:
            board[row][col] = PLAYER_O
        else:
            print("Invalid move, try again.")
            continue

        # Check for a winner after human move
        if check_winner(board) == PLAYER_O:
            print_board(board)
            print("You win!")
            break
        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # AI move (Player X)
        print("AI is making a move...")
        ai_row, ai_col = best_move(board)
        board[ai_row][ai_col] = PLAYER_X

        # Check for a winner after AI move
        if check_winner(board) == PLAYER_X:
            print_board(board)
            print("AI wins!")
            break
        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

# Run the game
play_game()
