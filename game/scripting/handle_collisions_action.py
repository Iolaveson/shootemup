import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the robot collides
    with the food, or the robot collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            # self._handle_bullet_collision(cast)
            self._handle_robot_collision(cast)
            self._handle_game_over(cast)

    # def _handle_bullet_collision(self, cast):
    #     """Updates the score nd moves the food if the robot collides with the food.
        
    #     Args:
    #         cast (Cast): The cast of Actors in the game.
    #     """
    #     score = cast.get_first_actor("scores")
    #     food = cast.get_first_actor("foods")
    #     # robot = cast.get_first_actor("robot")
    #     bullet =  cast.get_first_actor('bullet')

    #     artifacts = cast.get_actors("artifacts")
    #     for item in artifacts:
    #         if bullet.get_position() == item.get_position():
    #             points = artifacts.calc_points()
    #             # robot.grow_tail(points)
    #             score.add_points(points)
    #             # food.reset()

    
    def _handle_robot_collision(self, cast):
        """Sets the game over flag if the robot collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        robot = cast.get_first_actor("robot")
        # hit_box = [robot.get_position()]
        # head = robot.get_segments()[0]
        # segments = robot.get_segments()[1:]
        
        # for segment in segments:
        #     if head.get_position().equals(segment.get_position()):
        artifacts = cast.get_actors("artifacts")
        for item in artifacts:
            if robot.get_position().equals(item.get_position()):
                self._is_game_over = True

    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the robot and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            robot = cast.get_first_actor("robot")
            # segments = robot.get_segments()
            artifacts = cast.get_actors("artifacts")

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)

            robot.set_color(constants.WHITE)
            for item in artifacts:
                item.set_color(constants.WHITE)