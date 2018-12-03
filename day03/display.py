import pyglet
from pyglet.window import key
from pyglet.window import mouse
from pyglet.gl import *
import re
import utils


# An animation of the claims being added sequentially
# The (pre-computed) non-overlapping claim is displayed in red


data = utils.load_data()
claims = {}
data_i = 0


# Window parameters
width  = 800
height = 800
scale  = 800.0/1000
window = pyglet.window.Window(width, height)
glClearColor(1, 1, 1, 1)


# Drawing
@window.event
def on_draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    
    glPushMatrix()
    glScalef(scale,scale,scale) # Scale coordinates, so we can draw points according to their model coordinates and fill the window

    for id_, c in claims.items():
        if id_ == 625 and data_i == len(data):
            glColor4f(1, 0, 0, 1.0)
        else:
            glColor4f(0, 0, 0, 0.2)
        glRectf(c.x, c.y, c.x+c.w, c.y+c.h)

    glPopMatrix()

    
# Periodically called
def update(dt):
    global data_i

    for i in range(3):
        if data_i < len(data):
            id_, x, y, w, h = map(int, re.search(utils.re_str, data[data_i]).groups())
            claims[id_] = utils.Claim(x, y, w, h)
            data_i += 1


pyglet.clock.schedule(update)
pyglet.app.run()


