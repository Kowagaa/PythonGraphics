import time
import os
import ast

class pixel:
    def __init__(self, color : int):
        self.color = color
        self.display = f"\033[4{color}m   \033[0m"

class bitMap:
    def __init__(self, pixels : list[list[pixel]]):
        """
        Pixels in (y, x) format
        """
        self.pixels = pixels
        self.x = len(pixels[0])
        self.y = len(pixels)
    def display(self):
        out = ""
        for i in range(len(self.pixels)):
            for j in range(len(self.pixels[i])):
                out += self.pixels[i][j].display
            out += "\n"
        return out
    
class bitAnim:
    def __init__(self, frames : list[bitMap]):
        self.curr = 0
        self.frames = frames
    def displayFrame(self):
        if curr >= len(self.frames):
            curr = 0
        curr += 1
        return self.frames[curr - 1]

class backDrop:
    def __init__(self, bitmap : bitMap):
        self.bitmap = bitmap
    
    def superpose(self, overbitmap : bitMap, coordinates : tuple[int]):
        """
        Coordinates in (y, x) format
        """
        for i in range(overbitmap.y):
            for j in range(overbitmap.x):
                self.bitmap[i + coordinates[0]][j + coordinates[1]] = overbitmap[i][j]

def arrToBitMap(values):
    for i in range(len(values)):
        for j in range(len(values[i])):
            values[i][j] = pixel(values[i][j])
    return bitMap(values)

def writeBitMapToStr(bitmap : bitMap):
    out = [[0 for i in range(bitmap.y)] for i in range(bitmap.x)]
    for i in range(bitmap.y):
        for j in range(bitmap.x):
            out[i][j] = bitmap.pixels[i][j].color
    return out

def saveToDotpybm(bitmap : bitMap, path : str):
    out = writeBitMapToStr(bitmap)
    with open(path, "w") as f:
        f.write(str(out))
        print(ast.literal_eval(str(out)))

a = backDrop(arrToBitMap([[3 for i in range(10)] for i in range(10)]))

def refresh():
    os.system("cls")
    print(a.bitmap.display())

while True:
    time.sleep(0.05)
    refresh()