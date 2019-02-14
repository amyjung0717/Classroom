import arcade


WIDTH = 640
HEIGHT = 480

x = int(input("Enter x location: "))
y = int(input("Enter y location: "))
radius = int(input("Enter the radius of the circle: "))

arcade.open_window(WIDTH, HEIGHT, "My Drawing")
arcade.set_background_color(arcade.color.BABY_BLUE)

arcade.start_render()
# Begin drawing

arcade.draw_circle_filled(x, y, radius, arcade.color.DARK_BLUE_GRAY)

# End drawing
arcade.finish_render()
arcade.run()