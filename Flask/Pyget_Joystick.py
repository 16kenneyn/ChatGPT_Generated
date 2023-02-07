import pyglet
from pyglet.window import key
from pyglet.window import Window
from pyglet.input import get_joysticks

window = Window()
joysticks = get_joysticks()

if joysticks:
    joystick = joysticks[0]
    joystick.open()

@window.event
def on_draw():
    window.clear()

@window.event
def on_joybutton_press(joystick, button):
    if button == 0:
        print("Button 0 pressed")

pyglet.app.run()
