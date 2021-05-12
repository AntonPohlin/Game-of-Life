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

import cell_class as cc  # noqa: E402


cell = cc.Cell(0, 0)


class TestCell(unittest.TestCase):

    def test_switch_state(self):
        cell = cc.Cell(0, 0)
        self.assertEqual(cell.state, 'dead')
        cell.switch_state()
        self.assertEqual(cell.state, 'alive')

    def test_get_colour(self):
        cell = cc.Cell(1, 2)
        alive_colour = [45, 200, 150]
        dead_colour = [10, 10, 10]
        cc.Cell.dead_colour = dead_colour
        cc.Cell.alive_colour = alive_colour
        self.assertEqual(cell.dead_colour, dead_colour)
        self.assertEqual(cell.alive_colour, alive_colour)

    def test_get_rect_info(self):
        new_x, new_y, new_state, new_width = 1, 2, 'dead', 10
        new_colour = [0, 0, 0]
        cell = cc.Cell(new_x, new_y, new_state)
        cc.Cell.cell_width = new_width
        cc.Cell.dead_colour = new_colour
        x, y, width, colour = cell.get_rect_info()
        self.assertEqual(x, new_x)
        self.assertEqual(y, new_y)
        self.assertEqual(width, new_width)
        self.assertEqual(colour, new_colour)

    def test_set_next_state(self):
        cell = cc.Cell(0, 0, 'dead')
        next_state = 'alive'
        cell.next_state = next_state
        cell.set_next_state()
        self.assertEqual(cell.state, 'alive')


# run unittest as main module and pass in test_cell_class
if __name__ == '__main__':
    unittest.main()
