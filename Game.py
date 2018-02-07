from GameBoard import GameBoard
from Clue import Clue
from Score import Score


class Game(object):
    """This is the highest level class which contains the Jeopardy, Double Jeopardy,
    and final Jeopardy rounds, as well as the player's score.
    """

    def __init__(self, clues):
        self.r1 = self.create_board(clues, 'Jeopardy!')
        self.r2 = self.create_board(clues, 'Double Jeopardy!')
        self.final_jeopardy_clue, self.final_jeopardy_category = self.get_final_jeopardy(clues)
        self.score = Score()

    def create_board(self, clues, round):
        return GameBoard(clues, round)

    def get_final_jeopardy(self, clues):
        for clue in clues:
            if clue['round'] == 'Final Jeopardy!':
                return Clue(clue['value'], clue['answer'], clue['question']), clue['category']

    def play(self):
        self.score = self.r1.play(self.score)
        self.score = self.r2.play(self.score)
        self.play_final_jeopardy()

    def play_final_jeopardy(self):
        print("\n\nFINAL JEOPARDY!\n")
        print("Category: " + self.final_jeopardy_category)
        wager = self.get_final_jeopardy_wager()
        self.final_jeopardy_clue.play()
        self.print_final_score(wager)

    def get_final_jeopardy_wager(self):
        while True:
            wager = input("\nEnter final Jeopardy wager: ")
            try:
                wager = int(wager)
                if wager < 0 or wager > self.score.score:
                    raise ValueError
                else:
                    return wager
            except ValueError:
                print("Invalid wager. Try again.")
                continue

    def print_final_score(self, wager):
        while True:
            correct = input("Enter '1' for correct or '0' for incorrect.")
            if correct is '1':
                self.score.update(wager)
                break
            elif correct is '0':
                self.score.update(wager * -1)
                break
        print("\n\nFinal score: $" + str(self.score.score))
