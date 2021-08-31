import random

def test1():
	random_integer = random.randint(1,10)
	print(random_integer)

	random_float = random.random() * 5
	print(random_float)

def exercise1():
	random_side = random.randint(0,1)
	if random_side == 1:
		print("Heads")
	else:
		print("Tails")

def test2():
	states_of_america = ["Delaware", "Pennsylvania", "New Jersey"]
	print(states_of_america)
	print(states_of_america[0])
	print(states_of_america[-1])
	states_of_america.append("Irvine")
	states_of_america.extend(["San Diego"])
	print(states_of_america)

def exercise2():
	name_string = input("Give me everybody's names, separated by a comma.\n")
	names = name_string.split(", ")
	num_items = len(names)
	print(names)
	random_name = random.randint(0, num_items-1)
	person_who_will_pay = names[random_name]
	print(f"{person_who_will_pay} is going to buy the meal today!")

def exercise3():
	row1 = [" ", " ", " "]
	row2 = [" ", " ", " "]
	row3 = [" ", " ", " "]
	map = [row1, row2, row3]
	print(f"{row1}\n{row2}\n{row3}")
	position = input("Where do you want to put the treasure?\n")

	horizonal = int(position[0])
	vertical = int(position[1])

	map[vertical-1][horizonal-1] = "X"

	print(f"{row1}\n{row2}\n{row3}")

def project1():
	rock = '''
		_______
	---'   ____)
		(_____)
		(_____)
		(____)
	---.__(___)
	'''

	paper = '''
		_______
	---'   ____)____
			______)
			_______)
			_______)
	---.__________)
	'''

	scissors = '''
		_______
	---'   ____)____
			______)
		__________)
		(____)
	---.__(___)
	'''
	user_win = 0
	computer_win = 0
	round = 0

	while round < 5:

		game_image =[rock, paper, scissors]

		round += 1
		print(f"Round: {round}")

		user_choice = int(input("What do you choose?\n(Type 0 for Rock, 1 for Paper, 2 for Scissors.)  \n"))
		if user_choice >= 3 or user_choice < 0:
			print("you typed an invalid number, you lose!")
			computer_win += 1
		else:
			print(game_image[user_choice])
		print(f"Total points: User:{user_win}, Computer: {computer_win} ")

		computer_choice = random.randint(0,2)
		print(f"Computer chose:")
		print(game_image[computer_choice])
		
		if user_choice == 0 and computer_choice == 2:
			print("You win!")
			user_win += 1

		elif computer_choice == 0 and user_choice == 2:
			print("You lose")
			computer_win += 1

		elif computer_choice > user_choice:
			print("You lose")
			computer_win += 1

		elif user_choice > computer_choice:
			print("You win!")
			user_win += 1

		elif user_choice == computer_choice:
			print("It's a draw")
		print(f"Total points: User:{user_win}, Computer: {computer_win} ")
	if user_win == computer_win:
		print("\n")
		print("Game is draw")
	elif user_win > computer_win:
		print("\n")
		print("You beat the computer!")
	else:
		print("\n")
		print("You lose. Try again!")
