import game_of_life_cy as GOL

# init
GOL.randomize_mode(True, 0.15)  # randomize with a factor of 0.1 alive cells
GOL.set_fps(60)  # set frames per second
GOL.set_window(1600, 900)  # set resolution (width x height)
GOL.set_cell_width(25)  # in pixels

'''
alternatively, change constants directly in
constants_cy.pyx and recompile

RANDOMIZE_CELLS = True
FACTOR_OF_ALIVE_CELLS = 0.15
FPS = 60
WIN_HEIGHT = 900
WIN_WIDTH = 900
CELL_WIDTH = 25
'''

# run
GOL.main()
