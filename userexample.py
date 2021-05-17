import game_of_life as GOL

GOL.randomize_cells(True, 0.1)  # Randomize with a factor of 0.1 alive cells
GOL.set_fps(500)
GOL.main()
