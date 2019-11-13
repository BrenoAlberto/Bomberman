class BombermanSimulacrum:
    def __init__(self, num_rows: int, num_cols: int, n_seconds: int, grid: []):
        """
        Args:
            num_rows: número de linhas.
            num_cols: número de colunas.
            n_seconds: número de segundos a serem simulados.
            grid: grid inicial onde a simulação ocorrerá

        """
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

    def increase_bomb_timer(self, i: int, j: int):
        """ Incrementa o timer da bomba, e caso alcançe 3 segundos de vida adiciona no mapa de bombas explodindo

        Args:
            i: linha.
            j: coluna.

        """
        if(self.grid[i][j] == 'O'):
            self.grid[i][j] = '1'

        elif(self.grid[i][j] == '1'):
            self.grid[i][j] = '2'

        elif(self.grid[i][j] == '2'):
            self.grid[i][j] = '3'
            self.exploding_bombs_map.append([i, j])

    def plant_bomb(self, i: int, j: int):
        """ Planta bomba no elemento ixj

        Args:
            i: linha.
            j: coluna.

        """
        self.grid[i][j] = 'O'

    def in_range(self, i: int, j: int) -> bool:
        """ Checa se o elemento ixj está nos limites do grid e é um elemento não bloqueante

        Args:
            i: linha.
            j: coluna.

        """

        if(i < 0 or j < 0 or i >= self.num_rows or j >= self.num_cols or self.grid[i][j] in ['X']):
            return False

        return True

    def locate_and_detonate_bombs(self):
        # """ Percorre o mapa de bombas explodindo  """
        if(len(self.exploding_bombs_map) > 0):
            for bomb_location in self.exploding_bombs_map:
                self.detonate_bomb(bomb_location[0], bomb_location[1])

            self.exploding_bombs_map.clear()

    def detonate_bomb(self, i: int, j: int):
        """ Explode toda a linha e coluna da bomba

        Args:
            i: linha da bomba.
            j: coluna da bomba.

        """
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

    def print_grid(self):
        """ Imprime o grid final no terminal  """
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
