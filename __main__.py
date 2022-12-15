from constants import CELL_SIZE, FONT_SIZE, ROWS, COLUMNS, DEFAULT_ARTIFACTS,  MAX_Y
import random

from game.casting.cast import Cast
from game.casting.artifact import Artifact
from game.casting.bullet import Bullet
from game.casting.score import Score
from game.casting.robot import Robot
from game.casting.food import Food
from game.casting.actor import Actor

from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point



def main():
    
    # create the cast
    cast = Cast()
    # cast.add_actor("bullet", Bullet(Point(0, MAX_Y -50)))
    cast.add_actor("foods", Food())
    cast.add_actor("robot", Robot())
    cast.add_actor("scores", Score())
    

    for n in range(DEFAULT_ARTIFACTS):
            objects = ['M','@']
            text = random.choice(objects)
            # message = messages[n]

            x = random.randint(1, COLUMNS - 1)
            y = random.randint(1, ROWS - 1)
            position = Point(x, y)
            position = position.scale(CELL_SIZE)

            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            color = Color(r, g, b)
            
            artifact = Artifact()
            artifact.set_text(text) #sets the shape of objects on screen
            artifact.set_font_size(FONT_SIZE)
            artifact.set_color(color)
            artifact.set_position(position)
            # artifact.set_message(message)
            artifact.set_velocity(Point(0,3))
            cast.add_actor("artifacts", artifact)
   
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()