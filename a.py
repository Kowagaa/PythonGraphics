from src.python_graphics_kowaga.graphics import graphics, file, conversion
from src.python_graphics_kowaga.utils import shapes

import time
import os

a = shapes.square((5, 5), 3, is_hollow= False)

def refresh():
    os.system('cls')
    print(a.display())
while True:
    time.sleep(1/20)
    refresh()