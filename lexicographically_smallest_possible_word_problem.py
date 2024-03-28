import numpy as np
def lexicographically_smallest_possible_word():
    pass

grid = []
for i in range(3):
    row = list(map(int, input().split()))
    grid.append(row)
print(grid[2])

def current_letters(grid):
    pass
def get_neighbors(row, col):
    # Define the possible neighboring cells
    neighbors = []
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if 0 <= row + dr < 3 and 0 <= col + dc < 3:
                # neighbors.append((row + dr, col + dc))
                neighbors.append(grid[row + dr][col + dc])
    return neighbors
a=int(input())
b=int(input())
print(get_neighbors(a, b))
