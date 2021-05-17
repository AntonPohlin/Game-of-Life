import cell_class as cc
import constants as C
import pygame
import psutil
import random


def get_RAMinfo():
    MB = 1048576
    RAMinfo = [int(n/MB) if n > 100 else n for n in psutil.virtual_memory()]
    return RAMinfo


def get_CPUinfo():
    return psutil.cpu_percent()


def get_data():
    data_dict = {}

    data_dict.update({'Iterations': [C.ITERATIONS, 0, 0]})
    data_dict.update({' Columns': [C.COLUMNS_OF_CELLS, 1, 0]})
    data_dict.update({' Rows': [C.ROWS_OF_CELLS, 2, 0]})
    data_dict.update({' Cells': [C.NUM_OF_CELLS, 3, 0]})
    data_dict.update({' Cell width': [C.CELL_WIDTH, 4, 0]})

    RAMinfo = get_RAMinfo()
    CPUinfo = get_CPUinfo()

    data_dict.update({'Tot RAM': [RAMinfo[0], 0, 1]})
    data_dict.update({' Avail RAM': [RAMinfo[1], 1, 1]})
    data_dict.update({' %RAM': [RAMinfo[2], 2, 1]})
    data_dict.update({' Used RAM': [RAMinfo[3], 3, 1]})
    data_dict.update({' CPU': [CPUinfo, 4, 1]})
    return data_dict


def get_cols_rows(win_width, win_height, cell_width):
    cols = win_width//cell_width
    rows = win_height//cell_width
    if cols < 1 or rows < 1:
        raise ValueError('Must have atleast one column AND row')
    return cols, rows


def create_cell_grid(columns, rows,
                     cell_width, cell_gap=2):
    coordinates_dict = {}

    if cell_width-cell_gap < 0:
        raise ValueError('Cell width must be positive!')
    cc.Cell.cell_width = cell_width-cell_gap
    for x in range(columns):
        for y in range(rows):
            cell_x_coord = x*cell_width
            cell_y_coord = y*cell_width
            if C.RANDOMIZE_CELLS:
                if random.uniform(0, 1) < C.FACTOR_OF_ALIVE_CELLS:
                    coordinates_dict.update({(x, y): cc.Cell(
                        cell_x_coord, cell_y_coord, 'alive')})
                else:
                    coordinates_dict.update({(x, y): cc.Cell(
                        cell_x_coord, cell_y_coord, 'dead')})
            else:
                coordinates_dict.update({(x, y): cc.Cell(
                    cell_x_coord, cell_y_coord)})
    return coordinates_dict


def get_cell_nextstate(cells_dict, coord):
    x = coord[0]
    y = coord[1]
    neighbours_coords = [(x-1, y-1), (x, y-1), (x+1, y-1),
                         (x-1, y), (x+1, y),
                         (x-1, y+1), (x, y+1), (x+1, y+1)]
    alive_neighbours = 0
    for i in range(len(neighbours_coords)):
        neighbour = cells_dict.get(neighbours_coords[i])

        # if neighbour is not None: # same as below, aka redundance??
        if neighbour:
            if neighbour.state == 'alive':
                alive_neighbours += 1

    # GoL RULE 1
    if cells_dict[coord].state == 'alive':
        if alive_neighbours < 2 or alive_neighbours > 3:
            cells_dict[coord].next_state = 'dead'
        else:
            cells_dict[coord].next_state = 'alive'

    # GoL RULE 2
    elif alive_neighbours == 3:
        cells_dict[coord].next_state = 'alive'

    # GoL RULE 3
    else:
        cells_dict[coord].next_state = 'dead'


def update_cell_grid_dims(win_width, win_height, cell_width):
    C.COLUMNS_OF_CELLS, C.ROWS_OF_CELLS = get_cols_rows(
        win_width, win_height, cell_width)
    if C.WIN_CLIP:
        C.WIN_WIDTH -= win_width % cell_width
        C.WIN_HEIGHT -= win_height % cell_width
    else:
        C.WIN_WIDTH = win_width
        C.WIN_HEIGHT = win_height
    C.CELL_WIDTH = cell_width
    C.CELL_GRID = create_cell_grid(
        C.COLUMNS_OF_CELLS, C.ROWS_OF_CELLS,
        C.CELL_WIDTH, C.CELL_GAP)
    C.ITERATIONS = 0


def drag(pos):
    column = int(pos[0]/C.CELL_WIDTH)
    row = int(pos[1]/C.CELL_WIDTH)
    clicked_cell = C.CELL_GRID.get((column, row))
    if clicked_cell:
        clicked_cell.state = C.MOUSE_CLICK_CELL_STATE


def next_iteration():
    for key in C.CELL_GRID:
        get_cell_nextstate(C.CELL_GRID, key)
    for key in C.CELL_GRID:
        C.CELL_GRID[key].set_next_state()
    C.ITERATIONS += 1


def draw_cell(screen):
    for key in C.CELL_GRID:
        cell = C.CELL_GRID.get(key)
        x, y, side_length, colour = cell.get_rect_info()
        Rect_Cell = pygame.Rect(x, y, side_length, side_length)
        pygame.draw.rect(screen, tuple(colour), Rect_Cell)


if __name__ == '__main__':
    get_data()
    get_CPUinfo()
