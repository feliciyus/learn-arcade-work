import arcade

arcade.open_window(800, 600, "lab02")

# Water
arcade.set_background_color((38, 32, 227))

arcade.start_render()

# Sand
arcade.draw_lrtb_rectangle_filled(0, 799, 200, 0, (224, 227, 170))

# Sky
arcade.draw_lrtb_rectangle_filled(0, 799, 600, 360, (131, 230, 228))

# Sun
arcade.draw_circle_filled(730, 530, 30, arcade.color.YELLOW)

# x, y lines
arcade.draw_line(730, 530, 730, 590, arcade.color.YELLOW, 2.5)
arcade.draw_line(730, 530, 730, 470, arcade.color.YELLOW, 2.5)
arcade.draw_line(730, 530, 790, 530, arcade.color.YELLOW, 2.5)
arcade.draw_line(730, 530, 670, 530, arcade.color.YELLOW, 2.5)
# Diagonal lines
arcade.draw_line(730, 530, 770, 570, arcade.color.YELLOW, 2.5)
arcade.draw_line(730, 530, 690, 490, arcade.color.YELLOW, 2.5)
arcade.draw_line(730, 530, 690, 570, arcade.color.YELLOW, 2.5)
arcade.draw_line(730, 530, 770, 490, arcade.color.YELLOW, 2.5)

# Birds

#arcade.draw_parabola_outline(100, 500, 150, 30, arcade.color.BLACK, 10)

arcade.draw_arc_outline(100, 500, 50, 50, arcade.color.BLACK, 0, 180, 4)

arcade.finish_render()

arcade.run()