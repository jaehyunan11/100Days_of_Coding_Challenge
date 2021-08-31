def test1():
	print("Welcome to the rollercoaster!")
	height = int(input("What is your height in cm?\n"))

	# = is assignment
	# == is checking quality
	
	if height >= 120:
		print("you can ride the rollercoaster!")
	else:
		print("Sorry. you have to grow taller before you can ride.")

def exercise1():
	number = int(input("Which number do you want to choose?\n"))

	if number % 2 == 0:
		print("This is an even number")
	else:
		print("This is odd number")

def test2():
	print("Welcome to the rollercoaster!")
	height = int(input("What is your height in cm?\n"))

	if height >= 120:
		print("You can ride the rollercoaster!")
		age = int(input("What is your age?\n"))
		if age > 12:
			print("Please pay $5")
		elif age <= 18:
			print("Please pay $7")
		else:
			print("Please pay $12")

	else:
		print("Sorry. you have to grow taller before you can ride.")

def exercise2():
	height = float(input("Enter your height in m:\n"))
	weight = float(input("Enter your eight in kg:\n"))

	bmi = round (weight / height ** 2)
	if bmi < 18.5:
		print(f"Your BMI is {bmi}, you are underweight")
	elif bmi < 25:
		print(f"Your BMI is {bmi}, you are a normal weight")
	elif bmi < 30:
		print(f"Your BMI is {bmi}, you are over weight")
	elif bmi < 35:
		print(f"Your BMI is {bmi}, you are obese")
	else:
		print(f"Your BMI is {bmi}, you are clinically obese")

def exercise3():
	year = int(input("Which year do you want to check?\n"))

	if year % 4 == 0:
		if year % 100 == 0:
			if year % 400 == 0:
				print(f"{year} is leap year")
			else:
				print(f"{year} is not leap year!")
		else:
			print(f"{year} is not leap year!")

	else:
		print(f"{year} is not leap year!")

def exercise4():
	print("Welcome to the rollercoaster!")
	height = int(input("What is your height in cm?\n"))
	bill = 0

	if height >= 120:
		print("You can ride the rollercoaster!")
		age = int(input("What is your age?\n"))
		if age < 12:
			bill =5
			print("Child tickets are $5")
		elif age <= 18:
			bill = 7
			print("Youth tickets are $7")
		else:
			bill = 12
			print("Adult tickets are $12")

		wants_photo = input("Do you want a photo taken? Y or N.")
		if wants_photo == "Y":
			bill += 3 
		print(f"Your final bill is ${bill}")

	else:
		print("Sorry. you have to grow taller before you can ride.")

def exercise5():
	print("Welcome to Python Pizza Deliveries!")
	size = input("What size pizza do you wnat? S, M, or L\n")
	add_pepperoni = input("Do you want pepperoni? Y or N\n")
	extra_cheese = input("Do you want extra cheese? Y or N\n")

	bill = 0
	
	if size == "S":
		bill += 15
	elif size == "M":
		bill += 20
	elif size == "L":
		bill += 25
	if add_pepperoni == "Y":
		if size == "S":
			bill += 2
		else:
			bill += 3
	if extra_cheese == "Y":
		bill += 1
	print(f"Your final bill is ${bill}")

def exercise6():
	print("Welcome to the rollercoaster!")
	height = int(input("What is your height in cm?\n"))
	bill = 0

	if height >= 120:
		print("You can ride the rollercoaster!")
		age = int(input("What is your age?\n"))
		if age < 12:
			bill =5
			print("Child tickets are $5")
		elif age <= 18:
			bill = 7
			print("Youth tickets are $7")
		elif age >= 45 and age <= 55:
			print("Everything is going to be ok. Have a gree ride on us!")
		else:
			bill = 12
			print("Adult tickets are $12")

		wants_photo = input("Do you want a photo taken? Y or N.")
		if wants_photo == "Y":
			bill += 3 
		print(f"Your final bill is ${bill}")

	else:
		print("Sorry. you have to grow taller before you can ride.")

def exercise7():
	print("Welcome to the Love Calculator!")
	name1 = input("What is your name? \n")
	name2 = input("What is their name? \n")

	combined_string = name1 + name2
	lower_case_string = combined_string.lower()

	t = lower_case_string.count("t")
	r = lower_case_string.count("r")
	u = lower_case_string.count("u")
	e = lower_case_string.count("e")

	true = t + r + u + e

	l = lower_case_string.count("l")
	o = lower_case_string.count("o")
	v = lower_case_string.count("v")
	e = lower_case_string.count("e")

	love = l + o + v + e

	love_score = int(str(true) + str(love))

	print(love_score)

	if (love_score < 10) or (love_score > 90):
		print(f"Your score is {love_score}, you go together like coke and mentos")
	elif 40 <= love_score <= 50:
		print(f"Your score is {love_score}, you are alright together")
	else:
		print(f"Your score is {love_score}")


def project1():
	print("Welcome to Tresure Island!")
	print("Your mission is to find the treasure.")
	choice1 = input('You\'re at a crossroad, where do you want to go? Type "left" or "right".\n').lower()

	if choice1 == "left":
		# continue in the game
		choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
		if choice2 == "wait":
			choice3 = input("You arrived at the island unharmed. There is adhouse with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n").lower()
			if choice3 == "red":
				print("It's a room full of fire. Game Over.")
			elif choice3 == "yellow":
				print("You enter a room of beasts. Game Over.")
			else:
				print("You chose a door that doens't exist. Game Over.") 
		else:
			print("You got attached by an angry trout. Game Over")
	else:
		print("You fell into a hole. Game Over.")

