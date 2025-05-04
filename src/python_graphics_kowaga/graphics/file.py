from src.python_graphics_kowaga.graphics.graphics import *
from src.python_graphics_kowaga.graphics.conversion import *
from ast import literal_eval

def saveToDotpybm(bitmap : bitMap, path : str):
    out = bitMapToArr(bitmap)
    with open(path, "w") as f:
        f.write(str(out))

def saveToDotpyanim(bitanim : bitAnim, path : str):
    out = [bitMapToArr(bitanim.frames[i]) for i in range(bitanim.length)]
    with open(path, "w") as f:
        f.write(str(out))

def readDotpybm(path : str):
    with open(path, 'r') as f:
        return arrToBitMap(f.read())

def saveToDotpyanim(path : str):
    with open(path, 'r') as f:
        out = literal_eval(f.read())
        return bitAnim([bitMap(item)for item in out])