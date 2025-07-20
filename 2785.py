#https://github.com/malbolgee/URI/blob/master/2785.c
#Solved using chatgpt

import numpy as np

MAXSIZE = 101

# Dynamic programming
matrix = np.zeros((MAXSIZE, MAXSIZE), dtype=int)
memory = np.full((MAXSIZE, MAXSIZE), -1, dtype=int)

def calculate(row, column):
    total = 0

    # If the position [row][column] in the memory matrix is not -1
    # It means that this position has already been calculated, return this position
    if memory[row][column] != -1:
        return memory[row][column]

    # If it's the first row (base case), then return the memory matrix
    # with the element of the matrix at this position
    if row == 1:
        memory[row][column] = matrix[row][column]
        return memory[row][column]

    # Recurrence
    for i in range(row):
        total += matrix[row][column + i]

    memory[row][column] = total + min_val(calculate(row - 1, column), calculate(row - 1, column + 1))
    return memory[row][column]

def min_val(a, b):
    return min(a, b)

def main():
    matrix_size = int(input())

    for i in range(1, matrix_size + 1):
        row = list(map(int, input().split()))
        for j in range(1, matrix_size + 1):
            matrix[i][j] = row[j-1]

    # Fill the memory matrix with -1 to signal
    # That the value of the cell has not yet been calculated
    memory.fill(-1)

    print(calculate(matrix_size, 1))

if __name__ == "__main__":
    main()
