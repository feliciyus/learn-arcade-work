import arcade

WIDTH = 20
HEIGHT = 20
MARGIN = 5
ROW_COUNT = 10
COLUMN_COUNT = 10
SCREEN_WIDTH = (ROW_COUNT * WIDTH) + ((ROW_COUNT + 1) * MARGIN)
SCREEN_HEIGHT = (COLUMN_COUNT * HEIGHT) + ((COLUMN_COUNT + 1) * MARGIN)


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.BLACK)

        """
        # --- Create grid of numbers
        # Create an empty list
        self.grid = []
        # Loop for each row
        for row in range(ROW_COUNT):
            # For each row, create a list that will
            # represent an entire row
            self.grid.append([])
            # Loop for each column
            for column in range(COLUMN_COUNT):
                # Add a the number zero to the current row
                self.grid[row].append(0)
        """
        # This is simpler version of above
        self.grid = [[0 for x in range(10)] for y in range(10)]
        self.grid[1][5] = 1

    def on_draw(self):
        """
        Render the screen.
        """

        arcade.start_render()
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                if self.grid[row][column] == 1:
                    color = arcade.color.GREEN
                else:
                    color = arcade.color.WHITE
                x = (column * (WIDTH + MARGIN)) + MARGIN + WIDTH / 2
                y = (row * (HEIGHT + MARGIN)) + MARGIN + HEIGHT / 2
                arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        grid_row = y // (HEIGHT + MARGIN)
        grid_column = x // (WIDTH + MARGIN)

        print(f"Click coordinates: ({x}, {y}). Grid coordinates: ({grid_row}, {grid_column})")

        # Make sure we are on-grid. It is possible to click in the upper right
        # corner in the margin and go to a grid location that doesn't exist
        if grid_row < ROW_COUNT and grid_column < COLUMN_COUNT:

            # Flip the location between 1 and 0.
            if self.grid[grid_row][grid_column] == 0:
                self.grid[grid_row][grid_column] = 1
            else:
                self.grid[grid_row][grid_column] = 0


def main():

    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()