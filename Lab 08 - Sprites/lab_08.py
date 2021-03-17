import arcade
import random

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_STAR = 0.2
SPRITE_SCALING_ROCK = 0.2
STAR_COUNT = 50
ROCK_COUNT = 50
MOVEMENT_SPEED = 0

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Player(arcade.Sprite):
    

class Star(arcade.Sprite):

    def __init__(self, filename, sprite_scalling):
        super().__init__(filename, sprite_scalling)

        self.change_x = 0
        self.change_y = 0


class Rock(arcade.Sprite):

    def __init__(self, filename, sprite_scalling):
        super().__init__(filename, sprite_scalling)

        self.change_x = 0
        self.change_y = 0


class MyGame(arcade.Window):
    """ Window class"""

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Game 101")

        # Sprite lists
        self.player_list = None
        self.rock_list = None
        self.star_list = None

        # Player info

        self.player_sprite = None
        self.score = 0

    def setup(self):
        """ Set up the game and initialize the variables"""

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.rock_list = arcade.SpriteList()
        self.star_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        # Character image from kenney.nl
        self.player_sprite = arcade.Sprite("character_zombie_fallDown.png")
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0
        self.player_list.append(self.player_sprite)

        # Create the stars
        for i in range(STAR_COUNT):
            # Create star instance
            # Star image from kenney.nl
            star = Star("star.png", SPRITE_SCALING_STAR)
            self.star_list.append(star)
            # Stars falling down
            star.change_y -= 1

        for i in range(ROCK_COUNT):
            # Create rock instance
            # Rock image from kenney.nl
            rock = Star("ball_red_large.png", SPRITE_SCALING_ROCK)
            self.rock_list.append(rock)
            # Rocks going sideways
            rock.change_x -= 1

    def on_draw(self):
        arcade.start_render()

        # Drawing sprite lists
        self.star_list.draw()
        self.player_list.draw()
        self.rock_list.draw()

        # Drawing score
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)



    def update(self, delta_time):
        """ Movement and game logic """

        self.player_sprite.center_x += self.player_sprite.change_x
        self.player_sprite.center_y += self.player_sprite.change_y

        # Call update on all sprites
        self.star_list.update()
        self.rock_list.update()
        self.player_list.update()

        # Generate a list of all stars that collided with player
        star_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.star_list)
        # Same for rocks
        rock_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.rock_list)

        for star in star_hit_list:
            # Killing the star
            star.remove_from_sprite_lists()
            self.score += 1

        for rock in rock_hit_list:
            # Killing the rock
            rock.remove_from_sprite_lists()
            self.score -= 1

    def on_key_press(self, key, modifiers):
        """ Called when user presses a key """
        if key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0

def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()

