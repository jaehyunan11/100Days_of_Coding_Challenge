def first():
	print("day2")

def test1():
	print("123" + "345")

def test2():
	num_char = len(input("What is your name?\n"))
	new_num_char = str(num_char)
	print("Your name has " + new_num_char + " characters.")
	
def test3():
	a = 123
	print(type(a))

def exercise1():
	two_digit_number = input("Type a two digit number?\n")
	print(type(two_digit_number))
	first_digit = two_digit_number[0]
	second_digit = two_digit_number[1]
	print(first_digit)
	print(second_digit)
	result = int(first_digit) + int(second_digit)
	print(result)

def test4():
	print(type(6/3))
	print(6/3)
	print(2**3)
	print(3*3+3/3-3)

# PEMDAS
# ()
# **
# * /
# + -

def exercise2():
	height = input("Enter your height in m: \n")
	weight = input("Enter your weight in kg: \n")

	weight_as_int = int(weight)
	height_as_float = float(height)

	bmi = weight_as_int / height_as_float ** 2

	bmi_as_int = int(bmi)

	print(bmi_as_int)


def test5():
	# number of round 1,2,3 ...
	print(round(8/3, 1))
	# Floor division
	# return 2
	print(8 // 3)
	
	score = 0
	height = 1.8
	isWinning = True

	print("Your score is " + str(score))
	print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}")

def exercise3():
	age = input("What is your current age?\n")

	age_as_int = int(age)
	MAX_AGE = 100

	years_remaining = MAX_AGE - age_as_int
	days_remaining = years_remaining * 365
	weeks_remaining = years_remaining * 52
	months_remaining = years_remaining * 12

	message = f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left"

	print(message)

# If the bill was $150.00, split between 5 people, with 12% tip
# Each person should pay (150.00/5) * 1.12
# Round the result to 2 decimal places = 

def exercise4():
	print("Welcome to the tip calculator!")
	bill = float(input("What was th total bill? $\n"))
	tip = int(input("What percentage tip would you like to give? 10, 12, or 15?\n"))
	people = int(input("What many people to split the bill?\n"))

	tip_as_percent = tip / 100
	total_tip_amount = bill * tip_as_percent
	total_bill = bill + total_tip_amount
	bill_per_person = total_bill / people
	# final_amount = round(bill_per_person, 2)
	# round 2 method
	final_amount = "{:.2f}".format(bill_per_person)
	print(f"Each person should pay ${final_amount}")
	
