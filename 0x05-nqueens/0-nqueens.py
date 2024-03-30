#!/usr/bin/python3
import sys

def check_two_queens(new_queen_position, other_queen_position):
    if new_queen_position[0] == other_queen_position[0] or new_queen_position[1] == other_queen_position[1]:
        return False
    if new_queen_position[0] + new_queen_position[1] == other_queen_position[0] + other_queen_position[1]:
        return False
    if new_queen_position[0] - new_queen_position[1] == other_queen_position[0] - other_queen_position[1]:
        return False
    return True

def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == row - i:
            return False
    return True

def solve_nqueens(N, board, row, solutions):
    if row == N:
        solutions.append(board[:])
        return

    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(N, board, row + 1, solutions)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    N = int(sys.argv[1])
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * N
    solutions = []
    solve_nqueens(N, board, 0, solutions)

    for solution in solutions:
        print(solution)
