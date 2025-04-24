import time
import os
import ast

class pixel:
    def __init__(self, color : int):
        """
        Color is pixel color, -1 for transparent
        """
        self.color = color
        self.display = f"\033[4{color}m   \033[0m" if color != -1 else f"\033[0m   "

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
        self.length = len(frames)
        self.done = False
    def displayFrame(self):
        if self.curr >= len(self.frames):
            self.curr = 0
            self.done = True
        self.curr += 1
        return self.frames[self.curr - 1]

class backDrop:
    def __init__(self, bitmap : bitMap):
        self.bitmap = bitmap
    
    def superpose(self, overbitmap : bitMap, coordinates : tuple[int]):
        """
        Coordinates in (y, x) format
        """
        for i in range(overbitmap.y):
            for j in range(overbitmap.x):
                self.bitmap.pixels[i + coordinates[0]][j + coordinates[1]] = overbitmap.pixels[i][j]
