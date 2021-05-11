# Game of Life

Game of life shows how very simple rules can create very complex objects in an intuitive way. It was created by [John Horton Conway](https://en.wikipedia.org/wiki/John_Horton_Conway) in the 70s, a rather interesting person.

## Installation

The program needs [pygame](https://www.pygame.org/news) to work, use the package manager [pip](https://pip.pypa.io/en/stable/) to install pygame.

```bash
pip install pygame
```

## Usage

```python
import game_of_life as GOF

GOF.set_fps(50) #Default is 60 FPS
GOF.main() # to start the program

```
To toggle cells alive/dead simply click or drag over them

You can make the window larger/smaller by simply dragging with your mouse.

Press arrow key <kbd>Right</kbd> to iterate\
Press <kbd>Space</kbd> toggle run indefinitely\
Press <kbd>Up</kbd>/<kbd>Down</kbd> to increase/decrease the size of the cells

## Authors
Created by Anton Pohlin\
Contact: antonpohlin@gmail.com
## License

[MIT](https://choosealicense.com/licenses/mit/)
