class Cell:
    alive_colour = [50, 250, 150]
    dead_colour = [30, 30, 30]
    cell_width = 0

    def __init__(self, x, y, state='dead'):
        self.x = x
        self.y = y
        self.state = state
        self.next_state = state

    def get_rect_info(self):
        return self.x, self.y, Cell.cell_width, self.get_colour()

    def get_colour(self):
        if self.state == 'dead':
            return self.dead_colour
        elif self.state == 'alive':
            return self.alive_colour
        else:
            return -1

    def set_next_state(self):
        self.state = self.next_state

    def switch_state(self):
        if self.state == 'dead':
            self.state = 'alive'
        elif self.state == 'alive':
            self.state = 'dead'

    def __repr__(self):
        return f'Cell: {self.x}, {self.y}, {self.state}'

    def __str__(self):
        return f'Cell - Pos: {self.x}, {self.y} - State {self.state}'


if __name__ == '__main__':
    testcell = Cell(1, 2, 'dead')
    print(repr(testcell))
    print(str(testcell))
