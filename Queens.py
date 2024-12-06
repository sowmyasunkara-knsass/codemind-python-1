def solveNQueens(N):
    def is_safe(board, row, col):
        for i in range(row):
            if board[i] == col or abs(board[i] - col) == abs(i - row):
                return False
        return True

    def solve(board, row):
        if row == N:  
            result.append(['.' * i + 'Q' + '.' * (N - i - 1) for i in board])
            return
        
        for col in range(N):
            if is_safe(board, row, col):
                board[row] = col 
                solve(board, row + 1)  
                board[row] = -1  

    result = []
    board = [-1] * N  # Initialize the board (no queens placed)
    solve(board, 0)  
    return result
N = 4
solutions = solveNQueens(N)
for solution in solutions:
    for row in solution:
        print(row)
    print()
