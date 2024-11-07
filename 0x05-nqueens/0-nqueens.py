#!/usr/bin/python3
import sys

def print_solution(board):
    """Print a solution in the required format."""
    solution = []
    for i in range(len(board)):
        solution.append([i, board[i]])
    print(solution)

def is_safe(board, row, col):
    """Check if a queen can be placed on board[row][col]."""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(board, row, n):
    """Use backtracking to find all solutions for the n-queens problem."""
    if row == n:
        print_solution(board)
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(board, row + 1, n)
            board[row] = -1  # Backtrack

def nqueens():
    """Main function to parse input and initiate solving."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n  # Initialize board with -1, representing empty columns
    solve_nqueens(board, 0, n)

if __name__ == "__main__":
    nqueens()
