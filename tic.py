grid = [['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-']]
def print_grid(grid):
    for row in grid:
        for cell in row:
            print(cell, end=' ')
        print()
def check_win(grid, symbol):
    # Check rows
    for row in grid:
        if row.count(symbol) == 3:
            return True

    # Check columns
    for col in range(3):
        if grid[0][col] == symbol and grid[1][col] == symbol and grid[2][col] == symbol:
            return True

    # Check diagonals
    if grid[0][0] == symbol and grid[1][1] == symbol and grid[2][2] == symbol:
        return True
    if grid[0][2] == symbol and grid[1][1] == symbol and grid[2][0] == symbol:
        return True

    return False
def get_input(symbol):
    while True:
        try:
            row = int(input(f"Enter row for {symbol}: "))
            col = int(input(f"Enter column for {symbol}: "))
            if row >= 0 and row < 3 and col >= 0 and col < 3:
                return row, col
            else:
                print("Invalid row or column. Try again.")
        except ValueError:
            print("Invalid input. Try again.")
# Play the game
player1 = 'X'
player2 = 'O'
current_player = player1

while True:
    print_grid(grid)
    row, col = get_input(current_player)
    if grid[row][col] == '-':
        grid[row][col] = current_player
        if check_win(grid, current_player):
            print_grid(grid)
            print(f"{current_player} wins!")
            break
        elif '-' not in [cell for row in grid for cell in row]:
            print_grid(grid)
            print("It's a tie!")
            break
        else:
            current_player
