import arcade

arcade.open_window(800, 600, "lab02")

# Water
arcade.set_background_color((38, 32, 227))

arcade.start_render()

# Sand
arcade.draw_lrtb_rectangle_filled(0, 799, 200, 0, (224, 227, 170))

# Sky
arcade.draw_lrtb_rectangle_filled(0, 799, 600, 360, (131, 230, 228))

# --Sun--
# Base
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

# --Birds--
# Big bird
arcade.draw_arc_outline(100, 500, 50, 50, arcade.color.BLACK, 0, 180, 4)
arcade.draw_arc_outline(150, 500, 50, 50, arcade.color.BLACK, 0, 180, 4)

# Small birds
# Left
arcade.draw_arc_outline(70, 450, 30, 30, arcade.color.BLACK, 0, 180, 4)
arcade.draw_arc_outline(100, 450, 30, 30, arcade.color.BLACK, 0, 180, 4)
# Right
arcade.draw_arc_outline(150, 460, 30, 30, arcade.color.BLACK, 0, 180, 4)
arcade.draw_arc_outline(180, 460, 30, 30, arcade.color.BLACK, 0, 180, 4)

# --Clouds--
# Right
arcade.draw_ellipse_filled(550, 500, 200, 100, arcade.color.WHITE, 7)
arcade.draw_arc_filled(550, 535, 100, 50, arcade.color.WHITE, 0, 180)
arcade.draw_arc_filled(600, 525, 80, 80, arcade.color.WHITE, 0, 180, -20)

arcade.draw_arc_filled(550, 460, 100, 50, arcade.color.WHITE, 0, 180, 180)
arcade.draw_arc_filled(500, 475, 80, 80, arcade.color.WHITE, 0, 180, 160)

# Left
arcade.draw_ellipse_filled(320, 500, 200, 80, arcade.color.WHITE, -7)
arcade.draw_arc_filled(350, 530, 100, 50, arcade.color.WHITE, 0, 180)
arcade.draw_arc_filled(310, 525, 80, 80, arcade.color.WHITE, 0, 180, 20)
arcade.draw_arc_filled(275, 515, 80, 80, arcade.color.WHITE, 0, 180, 20)

arcade.draw_arc_filled(300, 480, 80, 80, arcade.color.WHITE, 0, 180, 160)
arcade.draw_arc_filled(360, 475, 100, 50, arcade.color.WHITE, 0, 180, 210)

# --Beach ball--
# Colors
arcade.draw_circle_filled(100, 100, 40, arcade.color.WHITE)
arcade.draw_arc_filled(100, 100, 80, 80, arcade.color.RED, 0, 60)
arcade.draw_arc_filled(100, 100, 80, 80, arcade.color.BLUE, 120, 180)
arcade.draw_arc_filled(100, 100, 80, 80, arcade.color.YELLOW, 240, 300)

# Middle and outline
arcade.draw_circle_outline(100, 100, 40, arcade.color.BLACK, 2)
arcade.draw_circle_filled(100, 100, 7, arcade.color.RED)

# --Beach umbrella--
# Shadow
arcade.draw_ellipse_filled(550, 100, 250, 100, (86, 87, 64))
# Handle and top
arcade.draw_rectangle_filled(550, 165, 10, 150, arcade.color.SILVER_PINK, 3)
arcade.draw_arc_filled(555, 235, 250, 100, (209, 27, 115), 0, 180, -3)
arcade.draw_triangle_filled(552, 285, 562, 285, 558, 295, arcade.color.SILVER_PINK)
# Stripes
arcade.draw_line(557, 285, 430, 241, arcade.color.BLACK, 2)
arcade.draw_line(557, 285, 500, 237, arcade.color.BLACK, 2)
arcade.draw_line(557, 285, 553, 235, arcade.color.BLACK, 2)
arcade.draw_line(557, 285, 600, 232, arcade.color.BLACK, 2)
arcade.draw_line(557, 285, 680, 229, arcade.color.BLACK, 2)
# Green Circles on top
arcade.draw_circle_filled(545, 260, 5, (47, 128, 66))
arcade.draw_circle_filled(535, 245, 5, (47, 128, 66))
arcade.draw_circle_filled(455, 260, 5, (47, 128, 66))
arcade.draw_circle_filled(495, 272, 5, (47, 128, 66))
arcade.draw_circle_filled(600, 257, 5, (47, 128, 66))
arcade.draw_circle_filled(620, 247, 5, (47, 128, 66))
# Blue Circles on top
arcade.draw_circle_filled(567, 253, 7, (71, 207, 214))
arcade.draw_circle_filled(490, 247, 7, (71, 207, 214))
arcade.draw_circle_filled(510, 260, 5, (71, 207, 214))
arcade.draw_circle_filled(650, 255, 5, (71, 207, 214))
arcade.draw_circle_filled(620, 265, 5, (71, 207, 214))

# --Boat--
# Base
arcade.draw_polygon_filled([[90, 300],
                            [140, 250],
                            [290, 250],
                            [340, 300]],
                           arcade.color.SIENNA)
# Mast (stovas)
arcade.draw_rectangle_filled(215, 390, 8, 180, (46, 46, 41))
# Jib (soninis stovas)
arcade.draw_triangle_filled(219, 310, 219, 480, 320, 310, (197, 182, 207))
# Boom (bure)
arcade.draw_rectangle_filled(165, 330, 100, 8, (46, 46, 41))
# Mail sail (galine bure)
arcade.draw_triangle_filled(125, 334, 211, 334, 211, 480, (197, 182, 207))
# Stays (virves)
arcade.draw_line(218, 479, 340, 300, arcade.color.BLACK, 2)
arcade.draw_line(212, 479, 90, 300, arcade.color.BLACK, 2)
# Name of boat
arcade.draw_text("KURSHIS", 140, 275, (115, 103, 122), 18)

arcade.finish_render()

arcade.run()
