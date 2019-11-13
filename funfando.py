
from time import sleep
import os
import pdb


class BombermanSimulacrum:
    def __init__(self, num_rows, num_cols, n_seconds, grid):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.n_seconds = n_seconds
        self.grid = grid
        self.exploding_bombs_map = []
        self.exploded_fields_map = []

    def start_simulation(self):
        for second in range(self.n_seconds + 1):
            for i in range(self.num_rows):
                for j in range(self.num_cols):
                    self.check_for_bomb_in_field(i, j)
                    if(second != 0 and second % 2 == 0 and self.grid[i][j] == '.'):
                        self.plant_bomb(i, j)
            if (second != 1 and second % 2 == 1):
                self.locate_and_detonate_bombs()

        self.print_grid()

    def check_for_bomb_in_field(self, i, j):
        if(self.grid[i][j] not in ['.', 'X']):
            self.increase_bomb_timer(i, j)

    def in_range(self, i, j):
        if(i < 0 or j < 0 or i >= self.num_rows or j >= self.num_cols):
            return False

        return True

    def plant_bomb(self, i, j):
        self.grid[i][j] = 'O'


    def increase_bomb_timer(self, i, j):
        if(self.grid[i][j] == 'O'):
            self.grid[i][j] = '1'
        elif(self.grid[i][j] == '1'):
            self.grid[i][j] = '2'
        elif(self.grid[i][j] == '2'):
            self.grid[i][j] = '3'
            self.exploding_bombs_map.append([i, j])

    def locate_and_detonate_bombs(self):
        if(len(self.exploding_bombs_map) > 0):
            for idx, bomb_location in enumerate(self.exploding_bombs_map):
                self.detonate_bomb(bomb_location[0], bomb_location[1])
                self.clear_exploded_fields()
            self.exploding_bombs_map.clear()
                # print('final')
                # self.print_grid()

    def detonate_bomb(self, i, j):
        self.grid[i][j] = '-'

        r, c = i, j
        while(r > 0):
            r = r - 1
            if(self.in_range(r, c) and not self.grid[r][c] in ['X']):
                self.grid[r][c] = '-'
                self.exploded_fields_map.append([r, c])
            else:
                break

        r, c = i, j
        while(r <= self.num_rows):
            r = r + 1
            if(self.in_range(r, c) and not self.grid[r][c] in ['X']):
                self.grid[r][c] = '-'
                self.exploded_fields_map.append([r, c])
            else:
                break

        r, c = i, j
        while(c > 0):
            c = c - 1
            if(self.in_range(r, c) and not self.grid[r][c] in ['X']):
                self.grid[r][c] = '-'
                self.exploded_fields_map.append([r, c])
            else:
                break

        r, c = i, j
        while(c <= self.num_rows):
            c = c + 1
            if(self.in_range(r, c) and not self.grid[r][c] in ['X']):
                self.grid[r][c] = '-'
                self.exploded_fields_map.append([r, c])
            else:
                break
        return

    def clear_exploded_fields(self):
        for idx, exploded_field in enumerate(self.exploded_fields_map):
            self.grid[exploded_field[0]][exploded_field[1]] = '.'

        self.exploded_fields_map.clear()

    def print_grid(self):
        print('\n'.join(''.join(*zip(*row)) for row in self.grid))

def get_input_grid():
    # rows >= 1
    # cols <= 200
    # n >= 1 n <= 10**9
    num_rows, num_cols, n_seconds = input().split()

    grid = []
    for _ in range(int(num_rows)):
        grid.append(list(input()))

    return int(num_rows), int(num_cols), int(n_seconds), grid


num_rows, num_cols, n_seconds, grid = get_input_grid()
bomberman_simulacrum = BombermanSimulacrum(num_rows, num_cols, n_seconds, grid)
bomberman_simulacrum.start_simulation()
