#write a code for a tic tac toe game 
#create a 3*3 grid for the game
#take input from the user for their move
#check for a win or a draw after each move 
#print the final result of the game

def print_board(board):
    """Display the current game board"""
    print("\n")
    for i in range(3):
        print(f" {board[i][0]} | {board[i][1]} | {board[i][2]} ")
        if i < 2:
            print("-----------")
    print("\n")

def is_winner(board, player):
    """Check if the given player has won"""
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    
    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
    
    return False

def is_board_full(board):
    """Check if the board is full"""
    return all(cell != " " for row in board for cell in row)

def get_move(board, player):
    """Get valid input from the user"""
    while True:
        try:
            move = int(input(f"Player {player}, enter position (1-9): "))
            if move < 1 or move > 9:
                print("Please enter a number between 1 and 9.")
                continue
            row, col = (move - 1) // 3, (move - 1) % 3
            if board[row][col] != " ":
                print("That position is already taken!")
                continue
            return row, col
        except ValueError:
            print("Please enter a valid number.")

def play_game():
    """Main game loop"""
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    print("Welcome to Tic Tac Toe!")
    print("Positions are numbered 1-9:")
    print(" 1 | 2 | 3")
    print("-----------")
    print(" 4 | 5 | 6")
    print("-----------")
    print(" 7 | 8 | 9")
    
    while True:
        print_board(board)
        row, col = get_move(board, current_player)
        board[row][col] = current_player
        
        if is_winner(board, current_player):
            print_board(board)
            print(f"🎉 Player {current_player} wins! 🎉")
            break
        
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break
        
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play_game()
