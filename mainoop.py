
from time import sleep
import os


class BombermanSimulacrum:
    def __init__(self, num_rows, num_cols, n_seconds, grid):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.n_seconds = n_seconds
        self.grid = grid
        self.exploding_bombs_map = []
        self.exploded_fields_map = []

    def start_simulation(self):
        for second in range(self.n_seconds):
            for i in range(self.num_rows):
                for j in range(self.num_cols):
                    self.__check_for_bomb_in_field(i, j)
            if (second % 2 == 0):
                # self.__plant_bombs_on_empty_fields()
            if (second != 1 and second % 2 == 1):
                self.__locate_and_detonate_bombs()

        print('\n'.join(''.join(*zip(*row)) for row in self.grid))

    def __check_for_bomb_in_field(self, i, j):
        if(self.grid[i][j] not in ['.', 'X']):
            self.__increase_bomb_timer(i, j)

    def __in_range(self, i, j):
        if(i < 0 or j < 0 or i >= self.num_rows or j >= self.num_cols or grid[i][j] == '-'):
            return False

        return True

    def __increase_bomb_timer(self, i, j):
        if(self.grid[i][j] == 'O'):
            self.grid[i][j] = '1'
        elif(self.grid[i][j] == '1'):
            self.grid[i][j] = '2'
        else:
            self.grid[i][j] = '3'
            self.exploding_bombs_map.append([i, j])

    def __locate_and_detonate_bombs(self):
        if(len(self.exploded_fields_map) > 0):
            for bomb_location in self.exploding_bombs_map:
                self.__detonate_bomb(bomb_location[0], bomb_location[1])
            self._clear_exploded_fields()

    def __detonate_bomb(self, i, j):
        if(not self.__in_range(i, j) or self.grid[i][j] == 'X'):
            return

        if(grid[i][j] in ['O', '1']):
            grid[i][j] = '-'
            self.exploded_fields_map.append([i, j])
            return

        grid[i][j] = '-'
        self.exploded_fields_map.append([i, j])

        self.__detonate_bomb(i + 1, j)
        self.__detonate_bomb(i - 1, j)
        self.__detonate_bomb(i, j + 1)
        self.__detonate_bomb(i, j - 1)
        return

    def _clear_exploded_fields(self):
        for exploded_field in self.exploded_fields_map:
            self.grid[exploded_field[0]][exploded_field[1]] = '.'


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
