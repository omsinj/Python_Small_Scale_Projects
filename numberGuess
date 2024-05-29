from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns):
    if guess > answer:
        print('Too high')
        return turns -1

    elif guess < answer:
        print('too low')
        return turns -1
    else:
        print(f"you got it. the answer is {answer}")


def set_difficulty():
    level = input("Please choose a diffculty, type 'easy' or 'hard'")
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print("Welcome to the number Guessing Game!")
    answer = randint(1,100)
    print(answer)

    turns = set_difficulty()
    

    guess = 0

    while guess != answer:
        guess = int(input("Make a guess: "))

        turns = check_answer(guess,answer, turns)
        print(f"You have {turns} attempts remaining to guess the number.")

        if turns  == 0:
            print('Game over, you lose')
            break
game()
