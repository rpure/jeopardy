from Clue import Clue
from texttable import Texttable


class GameBoard(object):
    """This class represents one round of play, e.g. Jeopardy or Double Jeopardy."""

    def __init__(self, clues, round):
        self.categories, self.board = self.populate_board(clues, round)

    def populate_board(self, clues, round):
        categories = {}
        board = [[None for i in range(5)] for j in range(6)]
        category_index = 0
        divisor = 200 if round == 'Jeopardy!' else 400
        for clue in clues:
            if clue['round'] == round:
                category = clue['category']
                if category not in categories:
                    categories[category] = category_index
                    category_index += 1
                clue = Clue(clue['value'], clue['answer'], clue['question'])
                try:
                    value_index = int(int(clue.value[1:])/divisor - 1)
                    board[categories[category]][value_index] = clue
                except ValueError:
                    pass
        return categories, board

    def play(self, score):
        while not self.check_complete():
            self.print_board()
            row, col = self.get_user_input()
            current_clue = self.board[row][col]
            current_clue.play()
            score = self.update_score(score, current_clue)
            self.board[row][col] = None
        print("Round complete!")
        return score

    def check_complete(self):
        for categories in self.board:
            for clue in categories:
                if clue is not None:
                    return False
        return True

    def get_user_input(self):
        while True:
            row = input("Enter row: ")
            col = input("Enter col: ")
            try:
                row = int(row)
                col = int(col)
                self.check_bad_input(row, col)
                return row, col
            except ValueError:
                print("Invalid input. Try again.")
                continue

    def check_bad_input(self, row, col):
        if row < 0 or row > 5:
            raise ValueError
        if col < 0 or col > 4:
            raise ValueError
        if self.board[row][col] is None:
            raise ValueError

    def update_score(self, score, clue):
        value = int(clue.value[1:])
        correct = input("Enter '1' for correct, '0' for incorrect, or anything else to pass. ")
        if correct is '1':
            score.update(value)
        elif correct is '0':
            score.update(value * -1)
        print("Current score: $" + str(score.score))
        return score

    def print_board(self):
        t = Texttable()
        categories_list = [None] * 6
        for key in self.categories:
            categories_list[self.categories[key]] = key
        t.add_row(categories_list)

        for i in range(5):
            values = []
            for j in range(6):
                if self.board[j][i] is not None:
                    values.append(self.board[j][i].value + " - " + str(j) + str(i))
                else:
                    values.append("x")
            t.add_row(values)

        print(t.draw())
