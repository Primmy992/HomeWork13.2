import json


class Result():
    def __init__(self, player_name, score, wrong_attempts, secret_number, date):
        self.player_name = player_name
        self.score = score
        self.wrong_attempts = wrong_attempts
        self.secret_number = secret_number
        self.date = date


def load_players(filename):
    try:
        with open(filename, "r") as score_file:
            return json.loads(score_file.read())
    except FileNotFoundError:
        return []


def save_game(filename, players):
    with open(filename, "w") as save_file:
        save_file.write(json.dumps(players, indent=4))


def check_guess(guess, secret, level, wrongguess):
    if guess > secret:
        if level == "easy":
            print("Your guess is not correct... try something smaller\n")
        else:
            print("Wrong!")
        wrongguess += 1
    elif guess < secret:
        if level == "easy":
            print("Your guess is not correct... try something bigger\n")
        else:
            print("Wrong!")
        wrongguess += 1
    return wrongguess