"""
This is a sample program to show how to draw using functions
"""

import arcade


def draw_grass():
    """
    This function draws the grass.
    """
    arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0, arcade.color.BITTER_LIME)


def draw_tree(x):
    """
    This function draws a pine tree.
    """
    
    # Draw the trunk
    arcade.draw_rectangle_filled(x+100, 200, 30, 80, arcade.color.BROWN)
    
    # Draw three levels of triangles
    arcade.draw_triangle_filled(x+50, 215, x+150, 215, x+100, 320, arcade.color.FOREST_GREEN)
    arcade.draw_triangle_filled(x+50, 255, x+150, 255, x+100, 360, arcade.color.FOREST_GREEN)
    arcade.draw_triangle_filled(x+60, 295, x+140, 295, x+100, 400, arcade.color.FOREST_GREEN)
                                
position = 0
arcade.open_window(800, 600, "Drawing with Functions")
arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)


def on_draw(delta_time):
    global position
    arcade.start_render()
    # Call our function to draw the grass
    draw_grass()
    draw_tree(position)
    arcade.finish_render()
    position += 1
arcade.schedule(on_draw, 1/60)
arcade.run()
