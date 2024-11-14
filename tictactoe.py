def initialize_board():
    """Create a fresh 3x3 board."""
    # Returns a new board filled with empty spaces for a fresh start
    return [[" " for _ in range(3)] for _ in range(3)]





def display_board(board):
    """Display the current state of the board."""
    # Prints each row of the board and a separator line after each row except the last
    for i, row in enumerate(board):
        print(" | ".join(row))  # Display the row with " | " between cells
        if i < 2:  # Only add separator after the first and second rows
            print("---------")  # Separator line for visual clarity





def check_winner(board, player):
    """Check if the specified player has won the game."""
    # Define winning patterns for rows, columns, and diagonals
    winning_patterns = [
        [board[i][j] == player for j in range(3)] for i in range(3)  # Rows
    ] + [
        [board[j][i] == player for j in range(3)] for i in range(3)  # Columns
    ] + [
        [board[i][i] == player for i in range(3)],  # Top-left to bottom-right diagonal
        [board[i][2 - i] == player for i in range(3)]  # Top-right to bottom-left diagonal
    ]
    
    # Return True if any winning pattern is met
    return any(all(pattern) for pattern in winning_patterns)





def get_valid_input(prompt):
    """Prompt user for a valid row or column input, handling range and type errors."""
    while True:
        try:
            value = int(input(prompt))  # Attempt to get an integer input
            if value not in [0, 1, 2]:  # Check if the input is within range
                print("Out of range. Please enter 0, 1, or 2.")
                continue
            return value  # Return the valid input
        except ValueError:
            print("Invalid input. Please enter a number.")  # Error message for non-integer input





def play_game(player_x, player_o):
    """Play a single game of Tic-Tac-Toe between two players."""
    # Initialize the board for each game
    board = initialize_board()
    current_symbol = "X"
    current_player = player_x  # Start with player X
    
    for _ in range(9):  # Loop for up to 9 moves (3x3 board)
        display_board(board)  # Show the current board
        
        # Get valid row and column inputs using the new helper function
        row = get_valid_input(f"{current_player} ({current_symbol}), enter the row (0, 1, or 2): ")
        col = get_valid_input(f"{current_player} ({current_symbol}), enter the column (0, 1, or 2): ")
        
        # Check if chosen cell is empty
        if board[row][col] != " ":
            print("This spot is taken. Try again.")
            continue
        
        # Place the current player's symbol on the board
        board[row][col] = current_symbol

        # Check if current player wins
        if check_winner(board, current_symbol):
            display_board(board)  # Show final board state
            print(f"{current_player} wins!")
            return current_player  # Return the winning player
        
        # Switch players and symbols for the next turn
        current_symbol = "O" if current_symbol == "X" else "X"
        current_player = player_o if current_player == player_x else player_x

    display_board(board)  # Display final board if it's a tie
    print("It's a tie!")
    return None  # Return None if there's no winner





def main():
    """Main function to play multiple games and track scores."""
    # Prompt players for their names
    player_x = input("Enter Player X's name: ")
    player_o = input("Enter Player O's name: ")
    
    # Initialize scores for both players
    scores = {player_x: 0, player_o: 0}
    
    while True:
        # Play a single game and capture the winner
        winner = play_game(player_x, player_o)
        if winner == player_x:
            scores[player_x] += 1  # Update score for player X
        elif winner == player_o:
            scores[player_o] += 1  # Update score for player O
        
        # Display the updated scores after each game
        print(f"Scores: {player_x} - {scores[player_x]}, {player_o} - {scores[player_o]}")
        
        # Ask players if they want to play again
        replay = input("Do you want to play again? (y/n): ").lower()
        if replay != 'y':
            print("Exiting game. Thanks for playing!")
            break  # Exit loop if players choose not to replay

# Run the main function to start the game
main()
