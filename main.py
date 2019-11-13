class BombermanSimulacrum:
    def __init__(self, num_rows, num_cols, n_seconds, grid):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.n_seconds = n_seconds
        self.grid = grid
        self.exploding_bombs_map = []

    def start_simulation(self):
        for second in range(self.n_seconds + 1):
            for i in range(self.num_rows):
                for j in range(self.num_cols):

                    if(self.grid[i][j] not in ['.', 'X']):
                        self.increase_bomb_timer(i, j)

                    if(second != 0 and second % 2 == 0 and self.grid[i][j] == '.'):
                        self.plant_bomb(i, j)

            if (second != 1 and second % 2 == 1):
                self.locate_and_detonate_bombs()

        self.print_grid()

    def increase_bomb_timer(self, i, j):
        if(self.grid[i][j] == 'O'):
            self.grid[i][j] = '1'

        elif(self.grid[i][j] == '1'):
            self.grid[i][j] = '2'

        elif(self.grid[i][j] == '2'):
            self.grid[i][j] = '3'
            self.exploding_bombs_map.append([i, j])

    def plant_bomb(self, i, j):
        self.grid[i][j] = 'O'

    def in_range(self, i, j):
        if(i < 0 or j < 0 or i >= self.num_rows or j >= self.num_cols or self.grid[i][j] in ['X']):
            return False

        return True

    def locate_and_detonate_bombs(self):
        if(len(self.exploding_bombs_map) > 0):
            for bomb_location in self.exploding_bombs_map:
                self.detonate_bomb(bomb_location[0], bomb_location[1])

            self.exploding_bombs_map.clear()

    def detonate_bomb(self, i, j):
        self.grid[i][j] = '.'

        r, c = i, j
        while(r > 0):
            r = r - 1
            if(not self.in_range(r, c)):
                break

            self.grid[r][c] = '.'

        r, c = i, j
        while(r <= self.num_rows):
            r = r + 1
            if(not self.in_range(r, c)):
                break

            self.grid[r][c] = '.'

        r, c = i, j
        while(c > 0):
            c = c - 1
            if(not self.in_range(r, c)):
                break

            self.grid[r][c] = '.'

        r, c = i, j
        while(c <= self.num_rows):
            c = c + 1
            if(not self.in_range(r, c)):
                break

            self.grid[r][c] = '.'
        return

    def print_grid(self):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                if(self.grid[i][j] in ['1', '2']):
                    self.grid[i][j] = 'O'

        print('\n'.join(''.join(*zip(*row)) for row in self.grid))

def get_input_grid():
    num_rows, num_cols, n_seconds = input().split()

    grid = []
    for _ in range(int(num_rows)):
        grid.append(list(input()))

    return int(num_rows), int(num_cols), int(n_seconds), grid


num_rows, num_cols, n_seconds, grid = get_input_grid()
bomberman_simulacrum = BombermanSimulacrum(num_rows, num_cols, n_seconds, grid)
bomberman_simulacrum.start_simulation()
