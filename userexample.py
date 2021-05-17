import game_of_life as GOL

# init
GOL.randomize_cells(True, 0.1)  # randomize with a factor of 0.1 alive cells
GOL.set_fps(50)  # set frames per second

# alternatively, change constants directly in constants.py
# RANDOMIZE_CELLS = True
# FACTOR_OF_ALIVE_CELLS = 0.1

# run
GOL.main()
