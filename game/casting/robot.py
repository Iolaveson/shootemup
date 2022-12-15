import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Robot(Actor):
    """
    A long limbless reptile.
    
    The responsibility of Robot is to move itself.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self):
        super().__init__()
        # self._segments = []
        # self._prepare_body()
        x = int(constants.MAX_X / 2)
        y = int(constants.MAX_Y -50)
        position = Point(x, y)
        velocity = Point(0, 0)
        # robot = Actor()
        self.set_position(position)
        self.set_velocity(velocity)
        self.set_text('W')
        self.set_color(constants.WHITE)
        

    # def get_segments(self):
    #     return self._segments

    # def move_next(self):
        # move all segments
        # for segment in self._segments:
        #     self.move_next()
        # update velocities
        # for i in range(len(self._segments) - 1, 0, -1):
        # trailing = self._segments[i]
        # previous = self._segments[i - 1]
        # velocity = previous.get_velocity()
        # trailing.set_velocity(velocity)

    # def move_next(self, max_x, max_y):
    #     """Moves the actor to its next position according to its velocity. Will wrap the position 
    #     from one side of the screen to the other when it reaches the given maximum x and y values.
        
    #     Args:
    #         max_x (int): The maximum x value.
    #         max_y (int): The maximum y value.
    #     """
    #     x = (self._position.get_x() + self._velocity.get_x()) % max_x #how to reset position 
    #     y = (self._position.get_y() + self._velocity.get_y()) % max_y
    #     self._position = Point(x, y)

    # def get_head(self):
    #     return self._segments[0]

    # def grow_tail(self, number_of_segments):
    #     for i in range(number_of_segments):
    #         tail = self._segments[-1]
    #         velocity = tail.get_velocity()
    #         offset = velocity.reverse()
    #         position = tail.get_position().add(offset)
            
    #         segment = Actor()
    #         segment.set_position(position)
    #         segment.set_velocity(velocity)
    #         segment.set_text("#")
    #         segment.set_color(constants.GREEN)
    #         self._segments.append(segment)

    def turn_head(self, velocity):
        self.set_velocity(velocity)
    
    def _prepare_body(self):
        x = int(constants.MAX_X / 2)
        y = int(constants.MAX_Y -50)

        # for i in range(constants.ROBOT_LENGTH):
        position = Point(x, y)
        velocity = Point(0, 0)
        # text = "8" if i == 0 else "#"
        # color = constants.YELLOW if i == 0 else constants.GREEN
        
        robot = Actor()
        robot.set_position(position)
        robot.set_velocity(velocity)
        robot.set_text('W')
        robot.set_color(constants.WHITE)
        # self._segments.append(segment)



        
        