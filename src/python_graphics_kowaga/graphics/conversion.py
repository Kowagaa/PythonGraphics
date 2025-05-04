from src.python_graphics_kowaga.graphics.graphics import *
def bitMapToArr(bitmap : bitMap):
    out = [[0 for i in range(bitmap.y)] for i in range(bitmap.x)]
    for i in range(bitmap.y):
        for j in range(bitmap.x):
            out[i][j] = bitmap.pixels[i][j].color
    return out

def arrToBitMap(values):
    for i in range(len(values)):
        for j in range(len(values[i])):
            values[i][j] = pixel(values[i][j])
    return bitMap(values)
