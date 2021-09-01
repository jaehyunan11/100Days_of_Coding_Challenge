from replit import clear
import random
from Day7 import hangman_words
from Day7 import hangman_art

def exercise1():
	end_of_game = False
	chosen_word = random.choice(hangman_words.word_list)
	word_length = len(chosen_word)
	# Lives are 6
	lives = 6
	#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word
	# For each letter in the chosen_word, add a "_" to display.
	# So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with "_" representing each letter to guess
	print(hangman_art.logo)
	# Testing code
	print(f"Psset, the solution is {chosen_word}")

	# Create blanks
	display = []
	word_length = len(chosen_word)
	for _ in range(word_length):
		display += "_"
	print(display)

	#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
	
	while not end_of_game:
		guess = input("Guess a letter: ").lower()

		clear()

		if guess in display:
			print(f"You've already guessed {guess}")

		# Check guessed letter
		for position in range(word_length):
			letter = chosen_word[position]
			# print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
			if letter == guess:
				display[position] = letter

		if guess not in chosen_word:
			print(f"You guessed {guess} that's not in the word. You lose a life.")
			lives -= 1
			if lives == 0:
				end_of_game = True
				print("***********")
				print("You lose!.")
				print("***********")

		print(f"{' '.join(display)}")

		if "_" not in display:
			end_of_game = True
			print("You win.")
		
		print(hangman_art.stages[lives])

	#TODO-3 - Check if the letter the user guessed(guess) is one of the letters in the chosen_word.
