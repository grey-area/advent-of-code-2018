import pyglet
from pyglet.window import key
from pyglet.window import mouse
from pyglet.gl import *
import re
from collections import namedtuple
import utils
import random


# An animation of the claims being added sequentially
# The (pre-computed) non-overlapping claim is displayed in green
# Includes silly Christmas themed animation


claims = utils.load_data()
claim_i = 0

class Snow():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
snow = [Snow(random.random()*1000, (1 + random.random())*1000) for i in range(1000)]
wind = 0.0


# Window parameters
width  = 800
height = 800
scale  = 800.0/1000
window = pyglet.window.Window(width, height)
glClearColor(0, 0, 0, 1)


# Drawing
@window.event
def on_draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    glPointSize(4 * scale)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    
    glPushMatrix()
    glScalef(scale,scale,scale) # Scale coordinates, so we can draw points according to their model coordinates and fill the window
    
    for id_, c in claims.items():
        if id_ > claim_i:
            break
        
        if id_ == 625 and claim_i == len(claims):
            glColor4f(0, 1, 0, 1.0)
        else:
            glColor4f(1, 0, 0, 0.2)
        glRectf(c.x, c.y, c.x+c.w, c.y+c.h)


    if claim_i == len(claims):
        glColor4f(1, 1, 1, 1.0)
        glBegin(GL_POINTS)
        for flake in snow:
            glVertex2f(flake.x, flake.y)
        glEnd()    

    glPopMatrix()

    
# Periodically called
def update(dt):
    global claim_i, wind

    if claim_i < len(claims):
        claim_i += 20
    else:
        claim_i = len(claims)

    if claim_i == len(claims):
        for flake in snow:
            flake.y -= 1 - 0.5 * random.random()
            if flake.y < 0:
                flake.y = 1000.0
            if flake.x < 0:
                flake.x = 1000.0
            elif flake.x > 1000:
                flake.x = 0.0
            flake.x += wind + 2 * (random.random() - 0.5) - 0.2
        wind += 0.2 * (random.random() - 0.5)
        wind *= 0.9


pyglet.clock.schedule_interval(update, 0.05)
pyglet.app.run()


