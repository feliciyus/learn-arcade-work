import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def draw_sand():
    """ Draw the ground """
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, (224, 227, 170))


def draw_sky():
    """ Draw the sky """
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT, 360, (131, 230, 228))


def draw_sun(x, y):
    """ Draw the sun """
    # Base
    arcade.draw_circle_filled(x, y, 30, arcade.color.YELLOW)

    # x, y lines
    arcade.draw_line(x, y, x, y + 60, arcade.color.YELLOW, 2.5)
    arcade.draw_line(x, y, x, y - 60, arcade.color.YELLOW, 2.5)
    arcade.draw_line(x, y, x + 60, y, arcade.color.YELLOW, 2.5)
    arcade.draw_line(x, y, x - 60, y, arcade.color.YELLOW, 2.5)
    # Diagonal lines
    arcade.draw_line(x, y, x + 40, y - 40, arcade.color.YELLOW, 2.5)
    arcade.draw_line(x, y, x - 40, y + 40, arcade.color.YELLOW, 2.5)
    arcade.draw_line(x, y, x - 40, y - 40, arcade.color.YELLOW, 2.5)
    arcade.draw_line(x, y, x + 40, y + 40, arcade.color.YELLOW, 2.5)


def draw_small_bird(x, y):
    """ Draw small bird """
    arcade.draw_arc_outline(x + 15, y, 30, 30, arcade.color.BLACK, 0, 180, 4)
    arcade.draw_arc_outline(x - 15, y, 30, 30, arcade.color.BLACK, 0, 180, 4)


def draw_big_bird(x, y):
    """ Draw big bird """
    arcade.draw_arc_outline(x + 25, y, 50, 50, arcade.color.BLACK, 0, 180, 4)
    arcade.draw_arc_outline(x - 25, y, 50, 50, arcade.color.BLACK, 0, 180, 4)


def draw_cloud_1(x, y):
    """ Draw 1st type cloud """
    arcade.draw_ellipse_filled(x, y, 200, 100, arcade.color.WHITE, 7)
    arcade.draw_arc_filled(x, y + 35, 100, 50, arcade.color.WHITE, 0, 180)
    arcade.draw_arc_filled(x + 50, y + 25, 80, 80, arcade.color.WHITE, 0, 180, -20)

    arcade.draw_arc_filled(x, y - 40, 100, 50, arcade.color.WHITE, 0, 180, 180)
    arcade.draw_arc_filled(x - 50, y - 25, 80, 80, arcade.color.WHITE, 0, 180, 160)


def draw_cloud_2(x, y):
    """ Draw 2nd type cloud"""
    arcade.draw_ellipse_filled(x, y, 200, 80, arcade.color.WHITE, -7)
    arcade.draw_arc_filled(x + 30, y + 30, 100, 50, arcade.color.WHITE, 0, 180)
    arcade.draw_arc_filled(x - 10, y + 25, 80, 80, arcade.color.WHITE, 0, 180, 20)
    arcade.draw_arc_filled(x - 45, y + 15, 80, 80, arcade.color.WHITE, 0, 180, 20)

    arcade.draw_arc_filled(x - 20, y - 20, 80, 80, arcade.color.WHITE, 0, 180, 160)
    arcade.draw_arc_filled(x + 40, y - 25, 100, 50, arcade.color.WHITE, 0, 180, 210)


def draw_beach_ball(x, y):
    """ Draw beach ball """
    # Colors
    arcade.draw_circle_filled(x, y, 40, arcade.color.WHITE)
    arcade.draw_arc_filled(x, y, 80, 80, arcade.color.RED, 0, 60)
    arcade.draw_arc_filled(x, y, 80, 80, arcade.color.BLUE, 120, 180)
    arcade.draw_arc_filled(x, y, 80, 80, arcade.color.YELLOW, 240, 300)

    # Middle and outline
    arcade.draw_circle_outline(x, y, 41, arcade.color.BLACK, 3)
    arcade.draw_circle_filled(x, y, 7, arcade.color.RED)


# 550 165
def draw_beach_umbrella(x, y):
    """ Draw an umbrella """
    # Shadow
    arcade.draw_ellipse_filled(x, y - 65, 250, 100, (86, 87, 64))
    # Handle and top
    arcade.draw_rectangle_filled(x, y, 10, 150, arcade.color.SILVER_PINK, 3)
    arcade.draw_arc_filled(x + 5, y + 70, 250, 100, (209, 27, 115), 0, 180, -3)
    arcade.draw_triangle_filled(x + 2, y + 120, x + 12, y + 120, x + 8, y + 130, arcade.color.SILVER_PINK)
    # Stripes
    arcade.draw_line(x + 7, y + 120, x - 120, y + 76, arcade.color.BLACK, 2)
    arcade.draw_line(x + 7, y + 120, x - 50, y + 72, arcade.color.BLACK, 2)
    arcade.draw_line(x + 7, y + 120, x + 3, y + 70, arcade.color.BLACK, 2)
    arcade.draw_line(x + 7, y + 120, x + 50, y + 67, arcade.color.BLACK, 2)
    arcade.draw_line(x + 7, y + 120, x + 130, y + 64, arcade.color.BLACK, 2)
    # Green Circles on top
    arcade.draw_circle_filled(x - 5, y + 95, 5, (47, 128, 66))
    arcade.draw_circle_filled(x - 15, y + 80, 5, (47, 128, 66))
    arcade.draw_circle_filled(x - 95, y + 95, 5, (47, 128, 66))
    arcade.draw_circle_filled(x - 65, y + 107, 5, (47, 128, 66))
    arcade.draw_circle_filled(x + 50, y + 92, 5, (47, 128, 66))
    arcade.draw_circle_filled(x + 70, y + 82, 5, (47, 128, 66))
    # Blue Circles on top
    arcade.draw_circle_filled(x + 17, y + 88, 7, (71, 207, 214))
    arcade.draw_circle_filled(x - 60, y + 82, 7, (71, 207, 214))
    arcade.draw_circle_filled(x - 40, y + 95, 5, (71, 207, 214))
    arcade.draw_circle_filled(x + 100, y + 88, 5, (71, 207, 214))
    arcade.draw_circle_filled(x + 70, y + 100, 5, (71, 207, 214))


def draw_boat(x, y):
    """ Draw a boat """
    # --Boat-- x = 215 y = 250
    # Base
    arcade.draw_polygon_filled([[x - 125, y + 50],
                                [x - 75, y],
                                [x + 75, y],
                                [x + 125, y + 50]],
                               arcade.color.SIENNA)
    # Mast (stovas)
    arcade.draw_rectangle_filled(x, y + 140, 8, 180, (46, 46, 41))
    # Jib (soninis stovas)
    arcade.draw_triangle_filled(x + 4, y + 60, x + 4, y + 230, x + 105, y + 60, (197, 182, 207))
    # Boom (bure)
    arcade.draw_rectangle_filled(x - 50, y + 80, 100, 8, (46, 46, 41))
    # Mail sail (galine bure)
    arcade.draw_triangle_filled(x - 90, y + 84, x - 4, y + 84, x - 4, y + 230, (197, 182, 207))
    # Stays (virves)
    arcade.draw_line(x + 3, y + 229, x + 125, y + 50, arcade.color.BLACK, 2)
    arcade.draw_line(x - 3, y + 229, x - 125, y + 50, arcade.color.BLACK, 2)
    # Name of boat
    arcade.draw_text("KURSHIS", x - 75, y + 25, (115, 103, 122), 18)


def on_draw(delta_time):
    """ Draw everything """
    arcade.start_render()

    draw_sand()
    draw_sky()
    draw_sun(on_draw.sun_x, 530)

    # Formula for sun to move
    on_draw.sun_x += on_draw.sun_delta_x * delta_time

    # If statement for sun to come out the other side
    if on_draw.sun_x - 80 > SCREEN_WIDTH:
        on_draw.sun_x = -80

    draw_small_bird(135, 495)
    draw_small_bird(60, 485)
    draw_big_bird(100, 530)
    draw_small_bird(690, 495)
    draw_small_bird(720, 475)
    draw_small_bird(760, 500)
    draw_cloud_1(300, 500)
    draw_cloud_2(500, 450)
    draw_beach_ball(550, 45)
    draw_beach_ball(270, 130)
    draw_beach_ball(150, 70)
    draw_boat(on_draw.boat_x, 250)

    # Formula for boat to move
    on_draw.boat_x += on_draw.boat_delta_x * delta_time

    # If statement for boat to keep coming back
    if on_draw.boat_x > 1000:
        on_draw.boat_delta_x *= -1
    if on_draw.boat_x < -400:
        on_draw.boat_delta_x *= -1

    draw_beach_umbrella(600, 200)


on_draw.sun_x = -80  # Starting sun position
on_draw.sun_delta_x = 200  # Speed of the sun
on_draw.boat_x = -399 # Starting boat position
on_draw.boat_delta_x = 100 # Speed of boat


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "lab03")
    # Water
    arcade.set_background_color((38, 32, 227))
    arcade.schedule(on_draw, 1 / 60)
    arcade.run()


if __name__ == "__main__":
    main()
