# Import the functions from the Draw 2-D library
# so that they can be used in this program.
'''Draw2d Documentation https://byui-cse.github.io/cse111-course/lesson03/draw2d.html'''
from turtle import circle, width, window_height, window_width
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing



def main():
    # Width and height of the scene in pixels
    window_width = 800
    window_height = 500

    # Call the start_drawing function in the draw2d.py library which will open a window and create a canvas.
    canvas = start_drawing("Scene", window_width, window_height)

    # Call your drawing functions
    # draw_sky 
    draw_sky(canvas, window_width, window_height)

    # # draw_ground
    draw_ground(canvas, window_width, window_height)

    # draw_pine_tree
    for x in range(100, 800, 100):
        peak_x, peak_y = draw_pine_tree(canvas, x, 100, 280)
        draw_circle(canvas, peak_x, peak_y, 15)

    # draw_cloud
    for x in range(150, 750, 100):
        draw_cloud(canvas, x, 410,450)
        draw_cloud(canvas, 100, 425, 460)

    # draw_grid
    # draw_grid(canvas, window_width, window_height, 50)

    # Call the finish_drawing function
    finish_drawing(canvas)

# draw_sky
def draw_sky(canvas, window_width, window_height):
    """Draw the sky and all the objects in the sky."""
    draw_rectangle(canvas, 0, window_height / 3,
        window_width, window_height, width = 0, fill="sky blue")

# draw ground
def draw_ground(canvas, window_width, window_height):
    """Draw the ground and all the objects on the ground."""
    draw_rectangle(canvas, 0, 0, window_width, window_height / 3, width = 0, fill="tan4" )

# draw pine tree
def draw_pine_tree(canvas, center_x, bottom, height):
    # draw the trunk of the tree
    trunk_width = height / 10
    trunk_height = height / 8
    left_trunk = center_x - trunk_width / 2 
    bottom_trunk = bottom
    right_trunk = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height
    draw_rectangle(canvas, left_trunk, bottom_trunk, right_trunk, trunk_top, width = 0, fill="saddleBrown")
    
    # draw skirt of tree
    skirt_width = height / 2
    skirt_left = center_x - skirt_width / 2
    skirt_bottom = trunk_top
    peak_x = center_x
    peak_y = bottom + height
    skirt_right = center_x + skirt_width / 2
    draw_polygon(canvas, skirt_left, skirt_bottom, peak_x, peak_y, skirt_right, skirt_bottom, width = 0, fill="green4")
    return peak_x, peak_y

# draw circle
def draw_circle(canvas, center_x, center_y, diameter):
    circle_radius = diameter / 2
    circle_x0 = center_x - circle_radius
    circle_x1 = center_x + circle_radius

    circle_y0 = center_y - circle_radius
    circle_y1 = center_y + circle_radius

    draw_oval(canvas, circle_x0, circle_y0, circle_x1, circle_y1, width = 0, fill="gold1")


def draw_grid(canvas, width, height, interval):

    #draw vertical line
    lable_y = 15
    for x in range(interval, width, interval):
        draw_line(canvas, x, 0, x, height)
        draw_text(canvas, x, lable_y, f"{x}")


    # draw horizontal line
    lable_x = 15
    for y in range(interval, height, interval):
        draw_line(canvas, 0, y, width, y)
        draw_text(canvas, lable_x, y, f"{y}")

# Draw a row of circles.
def draw_cloud(canvas,center_x, bottom, height):
    cloud_width = height / 19
    cloud_height = height / 19
    cloud_left = center_x - cloud_width / .5
    cloud_bottom = bottom
    cloud_right = center_x + cloud_width / .5
    cloud_top = bottom + cloud_height
    draw_oval(canvas, cloud_left, cloud_bottom, cloud_right, cloud_top, width = 0, fill="ghostWhite" )


main()