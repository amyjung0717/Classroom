"""
1. in the update function, use a loops to decrease the y positions by 1. To modify list values, you must use
square-bracket notation with the index location. eg. 'my list location'
"""

import random
import arcade

WIDTH = 650
HEIGHT = 480

star_x_positions = []
star_y_positions = []

for star in range(50):
    x = random.randrange(0, WIDTH)
    y = random.randrange(0, HEIGHT)
    star_x_positions.append(x)
    star_y_positions.append(y)

def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.BLACK)
    arcade.schedule(update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press
    arcade.run()


def update(delta_time):
    for index in range(len(star_x_positions)):
        #modify list using square-brakets and the index
        star_x_positions[index] += 5
        #read list values with square braket notation
        #eg. my_list 3
        if star_x_positions[index] == WIDTH:
            #modify list values using square braket notation
            star_y_positions[index] = random.randrange(0, HEIGHT)
            star_x_positions[index] = random.randrange(0,30)



def on_draw():
    arcade.start_render()

    for x, y in zip (star_x_positions, star_y_positions):
        arcade.draw_circle_filled(x, y, 5,arcade.color.ELECTRIC_YELLOW)



def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass


if __name__ == '__main__':
    setup()