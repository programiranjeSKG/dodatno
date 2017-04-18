''' tk_canvas_fractal_tree1.py
use the Tkinter canvas to draw a fractal tree

algorithm ...
draw the trunk
at the end of the trunk, split by some angle and draw two branches
repeat at the end of each branch until the desired branching is done
(dns)
'''

import math
import tkinter as tk
import random

def redraw():
    # clear the canvas
    canvas.delete('all')
    canvas.pack()
    # starting coordinates (x, y)
    x = w/2
    y = h - 10
    # starting angle
    angle =-90
    # experiment with length
    length = 10
    drawFractalTree(canvas, x, y, angle, length)

def drawFractalTree(canvas, x1, y1, angle, length):
    if length:
        x2 = x1 + int(math.cos(math.radians(angle)) * length * 10.0)
        y2 = y1 + int(math.sin(math.radians(angle)) * length * 10.0)
        canvas.create_line(x1, y1, x2, y2, fill="brown")
        # recursive calls
        drawFractalTree(canvas, x2, y2, angle - random.randint(10,20), length - 1)
        drawFractalTree(canvas, x2, y2, angle + random.randint(5,20), length - 1)

# create the main window
root = tk.Tk()
root.title("drawing a fractal tree")

# create the drawing canvas
w = 700
h = 600
canvas = tk.Canvas(root, width=w, height=h, bg='lightgreen')
redrawButton= tk.Button(root, text='redraw', command=redraw)
canvas.pack()
redrawButton.pack()

# starting coordinates (x, y)
x = w/2
y = h - 10
# starting angle
angle =-90
# experiment with length
length = 10
drawFractalTree(canvas, x, y, angle, length)

# start the GUI event loop
root.mainloop()
