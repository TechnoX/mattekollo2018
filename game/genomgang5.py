import arcade

arcade.open_window(800, 600, "Ett fint spel")

arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

arcade.start_render()

# Ansikte
arcade.draw_circle_filled(300,300, 200, arcade.color.YELLOW)

# Höger öga
arcade.draw_circle_filled(370, 350, 20, arcade.color.BLACK)

# Vänster öga
arcade.draw_circle_filled(230, 350, 20, arcade.color.BLACK)

# Mun
x = 300
y = 280
width = 120
height = 100
start_angle = 190
end_angle = 350
thickness = 10
arcade.draw_arc_outline(x, y, width, height, arcade.color.BLACK, start_angle, end_angle, thickness)

arcade.finish_render()

arcade.run()
