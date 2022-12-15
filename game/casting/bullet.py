from game.casting.actor import Actor
from game.shared.color import Color
from game.shared.point import Point
from game.casting.robot import Robot


class Bullet(Actor):
    '''Creates a bullet that is fired when spacebar is pressed
    '''
    def __init__(self, position):
        super().__init__()
        self._color = Color(200, 200, 200)
        self._text = "^"
        self._velocity = Point(0,-2)
        robot = Robot()
        self._position = position
        
        

    # def set_position(self, position):
    #     """Updates the position to the given one.
        
    #     Args:
    #         position (Point): The given position.
    #     """
    #     self._position = robot.position

    #construct bullet in this class

    