#!/usr/bin/python

# simple usage::
#   import colors
#   color = colors.Color
#   someObject(color.green)

class Color:

    white = (255,255,255)
    black = (0,0,0)
    red = (255,0,0)
    green = (0,255,0)
    blue = (0,0,255)
    yellow = (255,255,0)
    orange = (255,165,0)

    skyblue = (135,185,255)
    grassgreen = (100,255,100)
    dirtbrown = (229,137,71)

    def __init__(self):
        Color.white = Color.white
        Color.black = Color.black
        Color.red = Color.red
        Color.green = Color.green
        Color.blue = Color.blue
        Color.yellow = Color.yellow
        Color.orange = Color.orange

        Color.skyblue = Color.skyblue
        Color.dirtbrown = Color.dirtbrown
