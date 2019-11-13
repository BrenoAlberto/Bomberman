
from time import sleep
import os

def in_range(grid, i, j):
    num_rows, num_cols = len(grid), len(grid[0])

    # print(i)

    if(i < 0 or j < 0 or i >= num_rows or j >= num_cols):
	    return False

    return True

def detonate_bombs(grid, i, j):
    if(not in_range(grid, i, j) or grid[i][j] == 'X'):
        return 


    print('===============================')
    print('i', i)
    print('j', j)
    print('grid ixj', grid[i][j] )
    # print('i' = )
    print('===============================')

    if(grid[i][j] in ['O', '1'] ):
        grid[i][j] = '.'
        return

    grid[i][j] = '.'

    detonate_bomb(grid, i + 1, j)
    detonate_bomb(grid, i - 1, j)
    detonate_bomb(grid, i, j + 1)
    detonate_bomb(grid, i, j - 1)
    return     


def increase_bomb_timer(grid, i, j):
    if(grid[i][j] == 'O'):
        grid[i][j] = '1'
    elif(grid[i][j] == '1'):
        grid[i][j] = '2'
    else:
        grid[i][j] = '3'

def get_input_grid():
    # rows >= 1
    # cols <= 200
    # n >= 1 n <= 10**9
    num_rows, num_cols, n_seconds = input().split()


    grid = []
    for _ in range(int(num_rows)):
        grid.append(list(input()))
    
    return int(num_rows), int(num_cols), int(n_seconds), grid

# def check_grid():


def start_bomberman():
    num_rows, num_cols, n_seconds, grid = get_input_grid()
    for second in range(n_seconds):
        if(second != 0):
            for i in range(num_rows):
                for j in range(num_cols):
                    if(grid[i][j] not in ['.', 'X']):
                        increase_bomb_timer(grid, i, j)
            detonate_bombs(grid, i, j)
            # if (second % 2 == 0):
                # plant bombs
            # else if (second != 1 and second % 2 == 1):
                # detonate bombs
    print('\n'.join(''.join(*zip(*row)) for row in grid))

start_bomberman()
# os.system('cls' if os.name == 'nt' else 'clear')
# sleep(2) 
# print(grid)




[ 
    [0, 1, 2, 3],
    [0, 1, 2, 3],
    [0, 1, 2, 3],
    [0, 1, 2, 3],
]