from src.python_graphics_kowaga.graphics.graphics import *

def square(size : tuple[int], color : int, is_hollow : bool = True):
    """
    size should be in (y, x) format
    """
    if is_hollow:
        arr = [[pixel(-1) for i in range(size[0])] for j in range(size[1])]
        arr[0] = [pixel(color) for i in range(size[1])]
        arr[size[0]] = [pixel(color) for i in range(size[1])]
        for i in range(len(size[1])):
            arr[i][0] = pixel(color)
            arr[i][size[1]] = pixel(color)
        return bitMap(arr)
    else:
        return bitMap([[pixel(color) for i in range(size[0])] for j in range(size[1])])