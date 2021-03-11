import arcade

arcade.open_window(600, 600, "Drawing Example")

arcade.set_background_color(arcade.csscolor.LIGHT_CYAN)

arcade.start_render()

#Grass
arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.csscolor.GREEN)

#Tree trunk
arcade.draw_rectangle_filled(100, 320, 20, 60, arcade.csscolor.SIENNA)

#Tree trunk only outline
#arcade.draw_rectangle_outline(100, 320, 20, 60, arcade.csscolor.SIENNA, 3, 2)

#Tree Top
arcade.draw_circle_filled(100, 350, 30, arcade.csscolor.DARK_GREEN)

#Elipse correlation with rectangle
"""
arcade.draw_rectangle_outline(300, 300, 350, 200, arcade.csscolor.BLACK, 3)
arcade.draw_ellipse_outline(300, 300, 350, 200, arcade.csscolor.RED, 3)
"""

#Second tree, with a trunk and elipse on top of it
arcade.draw_rectangle_filled(200, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_ellipse_filled(200, 370, 60, 80, arcade.csscolor.DARK_GREEN)

#Third tree, with a trunk and arc
arcade.draw_rectangle_filled(300, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_arc_filled(300, 340, 80, 100, arcade.csscolor.DARK_GREEN, 0, 180)

#Another tree, with triangle

arcade.draw_rectangle_filled(400, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_triangle_filled(400, 400, 370, 320, 430, 320, arcade.csscolor.DARK_GREEN)

#Polygon tree

arcade.draw_rectangle_filled(500, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_polygon_filled(((500, 400),
                            (480, 360),
                            (470, 320),
                            (530, 320),
                            (520, 360)
                            ),
                           arcade.csscolor.DARK_GREEN)
#Sun
arcade.draw_circle_filled(500, 550, 40, arcade.color.YELLOW)
#Rays to x and y axis
arcade.draw_line(500, 550, 400, 550, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 600, 550, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 500, 450, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 500, 650, arcade.color.YELLOW, 3)
#Diagonal Rays
arcade.draw_line(500, 550, 550, 600, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 550, 500, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 450, 600, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 450, 500, arcade.color.YELLOW, 3)

#Text
arcade.draw_text("Pasodink medi!",
                 210, 230,
                 arcade.color.BLACK, 24)

#Code with parameter names
"""
arcade.draw_arc_outline(center_x=300,
                        center_y=340,
                        width=60,
                        height=100,
                        color=arcade.csscolor.BLACK,
                        start_angle=0,
                        end_angle=180,
                        border_width=3,
                        tilt_angle=45)
"""



arcade.finish_render()

arcade.run()