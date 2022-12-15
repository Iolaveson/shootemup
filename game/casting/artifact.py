from game.casting.actor import Actor

# TODO: Implement the Artifact class here. Don't forget to inherit from Actor!
class Artifact(Actor):

    def __init__(self):
        super().__init__()
        self._message = ''

    '''def get_message(self):
        return self._message
    
    def set_message(self,message):
        self._message = message'''

    def calc_point(self):
        '''determines points for each artifact
        '''
        score = 0

        if (self.get_text()) == 'M':
            score = 1
        elif (self.get_text()) == 'X':
            score = -3
        
        return score


        # artifact = Artifact()
        # artifact.set_text(text)
        # artifact.set_font_size(FONT_SIZE)
        # artifact.set_color(color)
        # artifact.set_position(position)
        # artifact.set_message(message)
        # cast.add_actor("artifacts", artifact)