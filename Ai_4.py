N = 4
def printSolution(board):

    for i in range(N):

        for j in range(N):
            print(board[i][j], end=' ')

        print()

def isSafe(board, row, col):

    # Check this row on left side
    for i in range(col):

        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1),
                    range(col, -1, -1)):

        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N),
                    range(col, -1, -1)):

        if board[i][j] == 1:
            return False

    return True

def solveNQUtil(board, col):
    if col >= N:
        return True

    # Try placing queen in all rows
    for i in range(N):

        # Check if queen can be placed safely
        if isSafe(board, i, col):

            # Place queen
            board[i][col] = 1

            # Recur to place rest of queens
            if solveNQUtil(board, col + 1):
                return True

            # Backtracking
            # Remove queen if solution not possible
            board[i][col] = 0

    return False

def solveNQ():
    board = [[0] * N for _ in range(N)]
    if not solveNQUtil(board, 0):

        print("Solution does not exist")
        return False

    printSolution(board)
    return True

solveNQ()