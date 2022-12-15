import random

from game.scripting.action import Action
from game.shared.point import Point
from game.shared.color import Color
from game.scripting.control_actors_action import ControlActorsAction
# from invaders.constants import CELL_SIZE, FONT_SIZE, ROWS, COLS, DEFAULT_ARTIFACTS
# from invaders.game.casting.artifact import Artifact

class DrawActorsAction(Action):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        score = cast.get_first_actor("scores")
        # food = cast.get_first_actor("foods")
        robot = cast.get_first_actor("robot")
        # segments = robot.get_segments()
        messages = cast.get_actors("messages")
        # trigger = ControlActorsAction()
        # if trigger.execute() is True:
        #     bullet = cast.get_first_actor('bullet')
        #     self._video_service.draw_actor(bullet)

        
        # for n in range(DEFAULT_ARTIFACTS):
        #     objects = ['M','X']
        #     text = random.choice(objects)
        #     # message = messages[n]

        #     x = random.randint(1, COLS - 1)
        #     y = random.randint(1, ROWS - 1)
        #     position = Point(x, y)
        #     position = position.scale(CELL_SIZE)

        #     r = random.randint(0, 255)
        #     g = random.randint(0, 255)
        #     b = random.randint(0, 255)
        #     color = Color(r, g, b)
            
        #     artifact = Artifact()
        #     artifact.set_text(text) #sets the shape of objects on screen
        #     artifact.set_font_size(FONT_SIZE)
        #     artifact.set_color(color)
        #     artifact.set_position(position)
        #     # artifact.set_message(message)
        #     artifact.set_velocity(Point(0,6))
        artifacts = cast.get_actors("artifacts")
        for n in artifacts:
            self._video_service.draw_actor(n)

        self._video_service.clear_buffer()
        # self._video_service.draw_actor(food)
        # self._video_service.draw_actor(artifact)
        # self._video_service.draw_actors(segments)
        self._video_service.draw_actor(robot)
        self._video_service.draw_actor(score)
        

        self._video_service.draw_actors(messages, True)
        self._video_service.flush_buffer()