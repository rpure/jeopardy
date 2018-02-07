class Score(object):
    """This class is used for tracking a single player's score.
    Functionality for multiple players may be added in a future version.
    """

    def __init__(self):
        self.score = 0

    def update(self, value):
        self.score += value
