from Day14.art import logo, vs
from Day14.game_data import data
import random
from replit import clear

def get_random_account():
	"""Get data from random account"""
	return random.choice(data)

def format_data(account):
	"""Takes the account data and returns the printable format."""
	name = account["name"]
	description = account["description"]
	country = account["country"]
	return (f"{name}, a {description}, from {country}")

def check_answer(guess, a_followers, b_followers):
	""" Checks followers against user's guess and return True if they got it right. Or False if they got it wrong.
	"""
	if a_followers > b_followers:
		return guess == "a"
	else:
		return guess == "b"

def game():
	# Display art 
	print(logo)
	score = 0
	game_should_continue = True
	account_a = get_random_account()
	account_b = get_random_account()
	# Make the game repeatable
	while game_should_continue:
		account_a = account_b
		account_b = get_random_account()

		while account_a == account_b:
			account_b = get_random_account()

		print(f"Compare A: {format_data(account_a)}.")
		print(vs)
		print(f"Compare B: {format_data(account_b)}.")


		# Ask user for a guess
		guess = input("Who has more followers? Type 'A' or 'B': ").lower()

		## Get follower count of each account
		a_follower_count = account_a["follower_count"]
		b_follower_count = account_b["follower_count"]
		## Use if statement to check if user is correct.
		is_correct = check_answer(guess, a_follower_count, b_follower_count)

		clear()
		print(logo)

		# Give user feedback on their guess
		if is_correct:
			score += 1
			print(f"You're right! Current score: {score}.")
		else:
			game_should_continue = False
			print(f"Sorry, that's wrong. Final score {score}")

game()

	# Score keeping

	# Make the game repeatable

	# Making account at posiiton B become the next account at possible

	# Add art

	# Clear screen between rounds