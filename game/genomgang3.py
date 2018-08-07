import arcade

arcade.open_window(600, 600, "Smiley")

arcade.set_background_color(arcade.color.WHITE)

arcade.start_render()

# Ansikte
arcade.draw_circle_filled(300,300,200, arcade.color.YELLOW)

# Höger öga
arcade.draw_circle_filled(370, 350, 20, arcade.color.BLACK)

# Vänster öga
arcade.draw_circle_filled(230, 350, 20, arcade.color.BLACK)

# Munnen
x = 300
y = 300
width = 120
height = 100
start_angle = 190
end_angle = 350
arcade.draw_arc_outline(x, y, width, height, arcade.color.BLACK, start_angle, end_angle, 10)



arcade.finish_render()

arcade.run()
