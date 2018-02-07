#Main file which begins game
from Game import Game
import json


def get_game(data):
    with open('episode_numbers.txt', 'r') as show_numbers:
        for show_number in show_numbers:
            print(show_number)

    requested_game = input("Which game would you like to play?\n")
    game_clues = []
    for entry in data:
        if entry['show_number'] == requested_game:
            game_clues.append(entry)
    return game_clues


def load_data():
    with open('JEOPARDY_QUESTIONS.json') as data_file:
        return json.load(data_file)

if __name__ == '__main__':
    data = load_data()
    clues = get_game(data)
    game = Game(clues)
    game.play()
