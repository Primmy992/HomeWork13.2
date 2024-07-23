import datetime
import json
import random

from functions import *

datum = datetime.datetime.now()
secret = random.randint(1, 30)
attempts = 0
wrongguess = 0

scoreList = load_players("score.json")

name = input("Enter your name: ")

while True:
    selection = input("Would you like to A) play a new game, B) see the bests cores, or C) quit?")
    while selection not in {'A', 'B', 'C'}:
        selection = input("Please provide valid input! Inputs: A or B or C")

    if selection == "A":
        level = input("Choose a difficulty level by entering ""hard"" or ""easy"": ")
        while level not in ("easy", "hard"):
            level = input("You've entered wrong option. Insert 'easy' or 'hard'")

        while True:
            guess = int(input(f"Guess the secret number (between 1 and 30): "))

            attempts += 1

            if guess == secret:
                print("\nYou've guessed it - congratulations! It's number " + str(secret))
                print("Attempts needed: " + str(attempts))
                print("Wrong attempts: " + str(wrongguess) + "\n")
                scoreData = Result(player_name=str(name), score=int(attempts), wrong_attempts=int(wrongguess),
                                   secret_number=int(secret), date=str(datum))

                scoreList.append(scoreData.__dict__)
                save_game("score.json", scoreList)

                break

            wrongguess = check_guess(guess, secret, level, wrongguess)

    elif selection == "B":
        def get_attempts(dictscore):
            return dictscore["score"]


        top_scores = sorted(scoreList, key=get_attempts)[:3]

        print("\nTop 3 Results:")
        identifier = 1
        for score in top_scores:
            print(f"{identifier}. {score['player_name']} - {score['score']} attempts on {score['date']}")
            identifier += 1
        print()
    else:
        break
