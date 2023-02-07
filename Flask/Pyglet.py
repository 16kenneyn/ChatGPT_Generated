import pyglet

# Create the window
window = pyglet.window.Window(width=800, height=600)

# Create a label for the title
title_label = pyglet.text.Label("Advanced Pyglet GUI Example",
                                 font_name='Times New Roman',
                                 font_size=36,
                                 x=window.width//2, y=window.height-50,
                                 anchor_x='center', anchor_y='center')

# Create a text box for input
input_text_box = pyglet.text.Label("Enter some text:",
                                    font_name='Times New Roman',
                                    font_size=24,
                                    x=50, y=window.height-100,
                                    anchor_x='left', anchor_y='center')
input_field = pyglet.text.Label("",
                                 font_name='Times New Roman',
                                 font_size=24,
                                 x=250, y=window.height-100,
                                 anchor_x='left', anchor_y='center')

# Create a button for submitting the input
submit_button = pyglet.text.Label("Submit",
                                   font_name='Times New Roman',
                                   font_size=24,
                                   x=500, y=window.height-100,
                                   anchor_x='center', anchor_y='center')

# Create a list for displaying the results
result_list = pyglet.text.Label("Results:",
                                 font_name='Times New Roman',
                                 font_size=24,
                                 x=50, y=window.height-200,
                                 anchor_x='left', anchor_y='center')
result_items = []

# Create a filter for the results
filter_label = pyglet.text.Label("Filter:",
                                  font_name='Times New Roman',
                                  font_size=24,
                                  x=50, y=window.height-300,
                                  anchor_x='left', anchor_y='center')
filter_field = pyglet.text.Label("",
                                  font_name='Times New Roman',
                                  font_size=24,
                                  x=150, y=window.height-300,
                                  anchor_x='left', anchor_y='center')
filter_button = pyglet.text.Label("Apply Filter",
                                   font_name='Times New Roman',
                                   font_size=24,
                                   x=500, y=window.height-300,
                                   anchor_x='center', anchor_y='center')

# Define the on_draw function to render the GUI elements
@window.event
def on_draw():
    window.clear()
    title_label.draw()
    input_text_box.draw()
    input_field.draw()
    submit_button.draw()
    result_list.draw()
    for item in result_items:
        item.draw()
    filter_label.draw()
    filter_field.draw()
    filter_button.draw()

pyglet.app.run()
