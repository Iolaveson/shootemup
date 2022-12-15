import constants
from game.scripting.action import Action
from game.shared.point import Point
from game.casting.bullet import Bullet
from game.casting.robot import Robot
# from game.services.video_service import VideoService


class ControlActorsAction(Action):
    """
    An input action that controls the snake.
    
    The responsibility of ControlActorsAction is to get the direction and move the snake's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction = Point(0, 0)

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        fire = False
        # left
        if self._keyboard_service.is_key_down('a'):
            self._direction = Point(-3, 0)
        
        # right
        if self._keyboard_service.is_key_down('d'):
            self._direction = Point(3, 0)

        #checks if spacebar is presses
        if self._keyboard_service.is_key_down('space'):
            robot = Robot()
            # fire = True
            player_location = robot.get_position()
            cast.add_actor("bullet", Bullet(player_location))
            bullet = cast.get_first_actor('bullet')
            # def _handle_bullet_collision(self, cast):
            """Updates the score nd moves the food if the robot collides with the food.
            
            Args:
                cast (Cast): The cast of Actors in the game.
            """
            score = cast.get_first_actor("scores")
            # food = cast.get_first_actor("foods")
            # robot = cast.get_first_actor("robot")
            # bullet =  cast.get_first_actor('bullet')

            artifacts = cast.get_actors("artifacts")
            for item in artifacts:
                if bullet.get_position() == item.get_position():
                    points = artifacts.calc_points()
                    # robot.grow_tail(points)
                    score.add_points(points)
                # food.reset()
            # v_s = VideoService()
            # v_s.draw_actor(bullet)
            # return fire
        
        # # up
        # if self._keyboard_service.is_key_down('w'):
        #     self._direction = Point(0, -constants.CELL_SIZE)
        
        # # down
        # if self._keyboard_service.is_key_down('s'):
        #     self._direction = Point(0, constants.CELL_SIZE)
        
        robot = cast.get_first_actor("robot")
        robot.turn_head(self._direction)

    # def get_trigger(self, cast):

    #     #checks if spacebar is presses
    #     if self._keyboard_service.is_key_down('SPACE'):
    #         fire = True
    #         cast.add_actor('bullet')
    #     return fire