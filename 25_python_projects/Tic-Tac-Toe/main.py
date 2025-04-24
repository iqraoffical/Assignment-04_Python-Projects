def draw_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_win(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in zip(*board):
        if all(cell == player for cell in col):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    for _ in range(9):
        draw_board(board)
        row = int(input(f"{player}, choose row (0-2): "))
        col = int(input(f"{player}, choose col (0-2): "))
        if board[row][col] == " ":
            board[row][col] = player
            if check_win(board, player):
                draw_board(board)
                print(f"{player} wins!")
                return
            player = "O" if player == "X" else "X"
        else:
            print("Invalid move, try again.")
    draw_board(board)
    print("It's a tie!")

tic_tac_toe()
