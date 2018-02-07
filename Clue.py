class Clue(object):
    """This class represents a single Jeopardy clue."""

    def __init__(self, value, answer, question):
        self.value = value
        self.answer = answer
        self.question = question

    def play(self):
        print("\n\nQUESTION: " + self.question + "\n\n")
        input("Press enter for answer.")
        print("\n\nANSWER: " + self.answer + "\n\n")
