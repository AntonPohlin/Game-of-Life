import unittest
import os
import sys
'''
To import cell_class.py, we need to first get the
PATH for the parent directory
'''
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

import helpers as h  # noqa: E402
import constants as C  # noqa: E402


class Testhelpers(unittest.TestCase):
    def test_get_cols_rows(self):
        cols, rows = h.get_cols_rows(140, 280, 14)
        self.assertEqual(cols, 10)
        self.assertEqual(rows, 20)
        with self.assertRaises(ValueError):
            h.get_cols_rows(0, 100, 5)
        with self.assertRaises(ValueError):
            h.get_cols_rows(100, 0, 5)
        with self.assertRaises(ValueError):
            h.get_cols_rows(100, 10, 50)

    def test_create_cell_grid(self):
        columns = 20
        rows = 10
        cell_width = 10
        cell_gap = 3
        cell_grid = {}
        C.FACTOR_OF_ALIVE_CELLS = False
        cell_grid = h.create_cell_grid(columns, rows, cell_width, cell_gap)
        self.assertEqual(len(cell_grid), columns*rows)
        for key in cell_grid:
            cell = cell_grid.get(key)
            # print('key: '+str(key))
            # print('x_coord: ' + str(cell.x))
            # print('y_coord: ' + str(cell.y))
            self.assertEqual(cell.x, key[0]*cell_width)
            self.assertEqual(cell.y, key[1]*cell_width)
            self.assertEqual(cell.cell_width, cell_width - cell_gap)

        with self.assertRaises(ValueError):
            h.create_cell_grid(columns, rows, 10, 20)  # if cell_gap>cell_width


# run unittest as main module and pass in test_cell_class
if __name__ == '__main__':
    unittest.main()
