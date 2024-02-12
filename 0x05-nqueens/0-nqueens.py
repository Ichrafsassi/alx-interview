#!/usr/bin/python3
import sys

def is_safe(board, row, col, N):
    # Check if there is a queen in the same column up to the current row
    for i in range(row):
        if board[i] == col:
            return False

        if abs(board[i] - col) == abs(i - row):
            return False

    return True

def solve_nqueens(N, row, board, solutions):
    if row == N:
        solutions.append(board[:])
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row] = col
            solve_nqueens(N, row + 1, board, solutions)

def print_solutions(solutions):
    for sol in solutions:
        print(sol)

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    board = [-1] * N
    solutions = []
    solve_nqueens(N, 0, board, solutions)
    print_solutions(solutions)

if __name__ == "__main__":
    main()
