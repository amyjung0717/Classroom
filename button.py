"""
Button Click
1. Figure out how you want to represent a button. Create global variable(s)
   for it.
2. Draw the button using the information stored in the button's variable(s).
3. In the on_mouse_press function, compare the mouse x and mouse y values to
   the values of the button to determine if there was a click or not.
"""

import arcade


WIDTH = 640
HEIGHT = 480

# Key for button index values
# This makes dealing with buttons as lists slightly easier.
BTN_X = 0
BTN_Y = 1
BTN_WIDTH = 2
BTN_HEIGHT = 3
BTN_IS_CLICKED = 4
BTN_COLOR = 5
BTN_CLICKED_COLOR = 6

# You might want to Google:
# - python namedtuple
# - python classes
# Those would be better ways to store objects like our button.
button1 = [200, 200, 300, 50, False, arcade.color.BLACK, arcade.color.WHITE]
button2 = [200, 130, 200, 50, False, arcade.color.BLUE, arcade.color.GREEN]
button3 = [200, 50, 200, 50, False, arcade.color.PINK, arcade.color.LIGHT_BLUE]
button4 = [300, 300, 200, 50, False, arcade.color.ORANGE, arcade.color.YELLOW]

def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press
    window.on_mouse_release = on_mouse_release

    arcade.run()


def update(delta_time):
    pass


def on_draw():
    arcade.start_render()
    # Draw in here...

    draw_button(button1)
    draw_button(button2)
    draw_button(button3)
    draw_button(button4)

def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    print(f"Click at ({x}, {y})")

    if mouse_is_over(x, y, button1):
        button1[BTN_IS_CLICKED] = True

    if mouse_is_over(x, y, button2):
        button2[BTN_IS_CLICKED] = True

    if mouse_is_over(x, y, button3):
        button3[BTN_IS_CLICKED] = True

    if mouse_is_over(x, y, button4):
        button4[BTN_IS_CLICKED] = True


def on_mouse_release(x, y, button, modifiers):
    # When you let go of the mouse, all buttons should be set to False.
    button1[BTN_IS_CLICKED] = False
    button2[BTN_IS_CLICKED] = False
    button3 [BTN_IS_CLICKED] = False
    button4 [BTN_IS_CLICKED] = False
def draw_button(button):
    # Select the appropriate color to draw with
    if button[BTN_IS_CLICKED]:
        color = button[BTN_CLICKED_COLOR]
    else:
        color = button[BTN_COLOR]

    # Draw button1
    arcade.draw_xywh_rectangle_filled(button[BTN_X],
                                      button[BTN_Y],
                                      button[BTN_WIDTH],
                                      button[BTN_HEIGHT],
                                      color)


def mouse_is_over(x, y, button):
    # Check if click happened on button
    if (x > button[BTN_X] and x < button[BTN_X] + button[BTN_WIDTH] and
            y > button[BTN_Y] and y < button[BTN_Y] + button[BTN_HEIGHT]):
        return True
    else:
        return False


if __name__ == '__main__':
    setup()