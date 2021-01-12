import random
EASY_LEVEL_ATTEMPTS=10
HARD_LEVEL_ATTEMPTS=5
def difficulty():
    difficulty = input("Choose a difficulty.Type 'easy' or 'hard':")
    if difficulty == "hard":
        return HARD_LEVEL_ATTEMPTS
    elif difficulty == "easy":
        return EASY_LEVEL_ATTEMPTS

def random_num_selector():
    num = random.randrange(1, 101)
    return num

def compare(guessed_num,random_num,turns):
    if guessed_num>random_num:
        print("Too High. Guess Again")
        turns-=1
        return turns
    elif guessed_num<random_num:
        print("Too Low. Guess Again")
        turns -= 1
        return turns
    elif guessed_num==random_num:
        print("You Guessed The Right Number.You Win!!!")

print("Welcome to the Number Guessing Game")
def game():
    print("I am thinking of a number between 1 and 100.")
    rand_num = random_num_selector()
    turns=difficulty()
    guess = 0
    while guess!=rand_num:
        print(f"You have {turns} attempts remaining to guess the number")
        guess=int(input("Make a Guess:"))
        turns=compare(guess,rand_num,turns)
        if turns==0:
            print("You used all of your attempts.You Lose")
            return
game()