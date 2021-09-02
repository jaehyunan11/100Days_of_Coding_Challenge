from random import randint
from Day12 import art

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
	"""checks answer against guess. Returns the number of turns remaining """
	if guess > answer:
		print("Too high")
		return turns - 1
	elif guess < answer:
		print("Too low")
		return turns - 1
	else:
		print(f"You got it! The answer was {answer}")

# Make function to set difficulty
def set_difficulty():
	level = input("Choose a difficutly. Type 'easy', 'hard' ")
	if level == "easy":
		return EASY_LEVEL_TURNS
	else:
		return HARD_LEVEL_TURNS
def game():
	print(art.logo)
	# Chooseing a random number between 1 to 100.
	print("Welcome to the Number Guessing Game!")
	print("I'm thinking of a number between 1 and 100.")
	answer = randint(1,100)
	print(f"pssst, the correct answer is {answer}")

	# Make function to set difficulty
	turns = set_difficulty()
	guess = 0

	while guess != answer:
		# Let the user guess a number
		print(f"You have {turns} attempts remaining to guess the number")
		guess = int(input("Make a guess: "))
		turns = check_answer(guess, answer, turns)
		if turns == 0:
			print("You've run out of guess. You lose")
			return
		elif guess != answer:
			print("Guess again!")

# Track the number of turns and reduce by 1 if they get it wrong.


game()