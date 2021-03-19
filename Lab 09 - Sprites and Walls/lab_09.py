import arcade
import random

# -- Constants --
# -- Walls --
# Used for first room walls
SPRITE_SCALING_1 = 1
# Used for second room walls
SPRITE_SCALING_2 = 0.5

SPRITE_NATIVE_SIZE = 64
SPRITE_SIZE = int(SPRITE_NATIVE_SIZE * SPRITE_SCALING_1)

# -- Player --
SPRITE_SCALING_PLAYER = 0.5
# Speed
MOVEMENT_SPEED = 5
UPDATES_PER_FRAME = 5
# Facing left or right
RIGHT_FACING = 0
LEFT_FACING = 1

# -- Stars --
SPRITE_SCALING_STAR = 0.8
STAR_COUNT = 25

# Resolution
SCREEN_WIDTH = SPRITE_SIZE * 14
SCREEN_HEIGHT = SPRITE_SIZE * 10


class Room:
    def __init__(self):
        self.wall_list = None

        self.background = None


def setup_room_1():

    room = Room()

    room.wall_list = arcade.SpriteList()
    room.star_list = arcade.SpriteList()

    # Top and bottom walls
    for y in (0, SCREEN_HEIGHT - SPRITE_SIZE):
        for x in range(0, SCREEN_WIDTH, SPRITE_SIZE):
            # Make a gap to the next room
            if (y == 0) or (x != SPRITE_SIZE * 7 and x != SPRITE_SIZE * 6):
                wall = arcade.Sprite("block_square.png", SPRITE_SCALING_1)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    # Left and right walls
    for x in (0, SCREEN_WIDTH - SPRITE_SIZE):
        for y in range(0, SCREEN_HEIGHT, SPRITE_SIZE):
            wall = arcade.Sprite("block_square.png", SPRITE_SCALING_1)
            wall.left = x
            wall.bottom = y
            room.wall_list.append(wall)

    # Middle rows
    for y in range(SPRITE_SIZE * 2, SCREEN_HEIGHT - SPRITE_SIZE, SPRITE_SIZE * 2):
        for x in range(0, SCREEN_WIDTH, SPRITE_SIZE):
            # Randomize gaps
            if x == SPRITE_SIZE * 6 or x == SPRITE_SIZE * 7:
                continue
            rand = random.randrange(0, 3)
            if rand < 2:
                wall = arcade.Sprite("block_square.png", SPRITE_SCALING_1)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    # Stars
    for i in range(STAR_COUNT):
        # Star image from kenney.nl
        star = Star("star.png", SPRITE_SCALING_STAR)
        star_placed_successfully = False
        while not star_placed_successfully:
            # Coin randomly anywhere
            star.center_x = random.randrange(SCREEN_WIDTH)
            star.center_y = random.randrange(SCREEN_HEIGHT)
            # Check if hits the wall
            wall_hit_list = arcade.check_for_collision_with_list(star, room.wall_list)
            # Check if hits another star
            star_hit_list = arcade.check_for_collision_with_list(star, room.star_list)

            if len(wall_hit_list) == 0 and len(star_hit_list) == 0:
                # Means not hitting any wall and other star
                star_placed_successfully = True
        room.star_list.append(star)

    # Background image from kenney.nl
    room.background = arcade.load_texture("skybox_sideHills.png")
    return room


def setup_room_2():

    room = Room()

    room.wall_list = arcade.SpriteList()
    room.star_list = arcade.SpriteList()

    # Top and bottom walls
    for y in (0, SCREEN_HEIGHT - SPRITE_SIZE):
        for x in range(0, SCREEN_WIDTH, SPRITE_SIZE):
            # Make a gap
            if (y != 0) or (x != SPRITE_SIZE * 6 and x != SPRITE_SIZE * 7):
                wall = arcade.Sprite("wood_red.png", SPRITE_SCALING_2)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    # Left and right walls
    for x in (0, SCREEN_WIDTH - SPRITE_SIZE):
        for y in range(0, SCREEN_HEIGHT, SPRITE_SIZE):
            wall = arcade.Sprite("wood_red.png", SPRITE_SCALING_2)
            wall.left = x
            wall.bottom = y
            room.wall_list.append(wall)

    # Top row where enemies are in the corners
    y = SPRITE_SIZE * 7
    for x in range(0, SCREEN_WIDTH, SPRITE_SIZE):
        # Make a gap
        if x != SPRITE_SIZE * 6 and x != SPRITE_SIZE * 7:
            wall = arcade.Sprite("wood_red.png", SPRITE_SCALING_2)
            wall.left = x
            wall.bottom = y
            room.wall_list.append(wall)

    # Random middle rows
    for y in range(SPRITE_SIZE * 2, SCREEN_HEIGHT, SPRITE_SIZE * 2):
        for x in range(0, SCREEN_WIDTH, SPRITE_SIZE):
            if x == SPRITE_SIZE * 6 or x == SPRITE_SIZE * 7 or y == SCREEN_HEIGHT - SPRITE_SIZE * 2:
                continue
            rand = random.randrange(0, 3)
            if rand < 2:
                wall = arcade.Sprite("wood_red.png", SPRITE_SCALING_2)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    # Stars
    for i in range(STAR_COUNT):
        # Star image from kenney.nl
        star = Star("star.png", SPRITE_SCALING_STAR)
        star_placed_successfully = False
        while not star_placed_successfully:
            # Coin randomly anywhere
            star.center_x = random.randrange(SCREEN_WIDTH)
            star.center_y = random.randrange(SCREEN_HEIGHT)
            # Check if hits the wall
            wall_hit_list = arcade.check_for_collision_with_list(star, room.wall_list)
            # Check if hits another star
            star_hit_list = arcade.check_for_collision_with_list(star, room.star_list)

            if len(wall_hit_list) == 0 and len(star_hit_list) == 0:
                # Means not hitting any wall and other star
                star_placed_successfully = True
        room.star_list.append(star)

    # Background image from kenney.nl
    room.background = arcade.load_texture("skybox_sideClouds.png")
    return room


def load_texture_pair(filename):
    """
    Load a texture pair, with the second being a mirror image.
    """
    return [
        arcade.load_texture(filename),
        arcade.load_texture(filename, flipped_horizontally=True)
    ]


class Player(arcade.Sprite):
    def __init__(self):
        super().__init__()

        # Default to face-right
        self.character_face_direction = RIGHT_FACING

        # Used for flipping between image sequences
        self.cur_texture = 0

        self.scale = SPRITE_SCALING_PLAYER

        # Adjust the collision box. Default includes too much empty space
        # side-to-side. Box is centered at sprite center, (0, 0)
        self.points = [[-22, -64], [22, -64], [22, 28], [-22, 28]]

        # --- Load Textures ---

        # Images from Kenney.nl
        main_path = "resources/character_maleAdventurer"

        # Load textures for idle standing
        self.idle_texture_pair = load_texture_pair(f"{main_path}_idle.png")

        # Load textures for walking
        self.walk_textures = []
        for i in range(8):
            texture = load_texture_pair(f"{main_path}_walk{i}.png")
            self.walk_textures.append(texture)

    def update_animation(self, delta_time: float = 1 / 60):

        # Figure out if we need to flip face left or right
        if self.change_x < 0 and self.character_face_direction == RIGHT_FACING:
            self.character_face_direction = LEFT_FACING
        elif self.change_x > 0 and self.character_face_direction == LEFT_FACING:
            self.character_face_direction = RIGHT_FACING

        # Idle animation
        if self.change_x == 0 and self.change_y == 0:
            self.texture = self.idle_texture_pair[self.character_face_direction]
            return

        # Walking animation
        self.cur_texture += 1
        if self.cur_texture > 7 * UPDATES_PER_FRAME:
            self.cur_texture = 0
        frame = self.cur_texture // UPDATES_PER_FRAME
        direction = self.character_face_direction
        self.texture = self.walk_textures[frame][direction]


class Star(arcade.Sprite):
    def __init__(self, filename, sprite_scaling):
        super().__init__(filename, sprite_scaling)


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 09 baby")

        # Sprite lists
        self.current_room = 0
        self.rooms = None
        self.player_list = None

        # Sounds
        self.star_sound = arcade.load_sound("Pickup__009.ogg")

        # Set up the player
        self.player_sprite = None
        self.score = 0

        # Physics engine
        self.physics_engine = None

        # Track the current state of what key is pressed
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

    def setup(self):
        # Sprite lists
        self.player_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Our list of rooms
        self.rooms = []
        # Room 1
        room = setup_room_1()
        self.rooms.append(room)
        # Room 2
        room = setup_room_2()
        self.rooms.append(room)

        self.current_room = 0

        # Set up the player
        # Character image from kenney.nl
        self.player_sprite = Player()
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 100
        self.player_list.append(self.player_sprite)

        # Player walking into room walls
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.rooms[self.current_room].wall_list)

    def on_draw(self):
        arcade.start_render()

        # Background
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.rooms[self.current_room].background)

        # Draw player
        self.player_sprite.draw()

        # Draw current room
        self.rooms[self.current_room].wall_list.draw()
        self.rooms[self.current_room].star_list.draw()

        # Drawing score
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.BLACK, 14)

        # Drawing gg
        game_over = "Game Over!"
        if len(self.rooms[0].star_list) == 0 and len(self.rooms[1].star_list) == 0:
            arcade.draw_text(game_over, SCREEN_WIDTH / 2 - 90, SCREEN_HEIGHT / 2, arcade.color.BLACK, 30)

    def update(self, delta_time):

        # Check if gg
        if len(self.rooms[0].star_list) > 0 or len(self.rooms[1].star_list) > 0:
            self.physics_engine.update()
            # Update walking animation
            self.player_list.update_animation()

        # Changing room logic
        if self.player_sprite.center_y > SCREEN_HEIGHT and self.current_room == 0:
            self.current_room = 1
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_y = 0
        elif self.player_sprite.center_y < 0 and self.current_room == 1:
            self.current_room = 0
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_y = SCREEN_HEIGHT

        # Collecting stars logic
        star_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.rooms[self.current_room].star_list)
        for star in star_hit_list:
            arcade.play_sound(self.star_sound)
            star.remove_from_sprite_lists()
            self.score += 1

        # Calculate speed based on the keys pressed
        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0

        # Keyboard movement logic
        if self.up_pressed and not self.down_pressed:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif self.down_pressed and not self.up_pressed:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        if self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_press(self, key, modifiers):
        """ Called when user presses a key """
        if key == arcade.key.UP:
            self.up_pressed = True
        elif key == arcade.key.DOWN:
            self.down_pressed = True
        elif key == arcade.key.LEFT:
            self.left_pressed = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = True

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.UP:
            self.up_pressed = False
        elif key == arcade.key.DOWN:
            self.down_pressed = False
        elif key == arcade.key.LEFT:
            self.left_pressed = False
        elif key == arcade.key.RIGHT:
            self.right_pressed = False


def main():
    """ MAIN """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
