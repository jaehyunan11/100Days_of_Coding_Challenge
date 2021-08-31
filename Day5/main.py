def test1():
	fruits = ["Apple", "Peach", "Pear"]
	for fruit in fruits:
		print(fruit)
		print(fruit + " Pie")

def exercise1():
	student_heights = input("Input a list of student heights?\n").split()

	for n in range(0, len(student_heights)):
		student_heights[n] = int(student_heights[n])
	print(student_heights)

	total_height = 0
	for height in student_heights:
		total_height += height
	print(total_height)

	number_of_students = 0
	for student in student_heights:
		number_of_students += 1
	print(number_of_students)


	# total_height = sum(student_heights)
	# number_of_students = len(student_heights)
	# average_height = round(total_height/number_of_students)
	# print(average_height)

def exercise2():
	student_scores = input("Input a list of student scores?\n").split()

	for n in range(0, len(student_scores)):
		student_scores[n] = int(student_scores[n])
	print(student_scores)

	# Method1

	# max_score = student_scores[0]

	# for n in range(0, len(student_scores)):
	# 	if student_scores[n] > max_score:
	# 		max_score = student_scores[n]
	# print(max_score)

	highest_score = 0
	for score in student_scores:
		if score > highest_score:
			highest_score = score
	print(f"The highest score in the class is: {highest_score}")

def test2():
	total = 0
	for number in range(1,101):
		total += number
	print(total)

def exercise3():
	total = 0
	for number in range(1,101):
		if number % 2 == 0:
			print(number)
			total += number
	print(total)

def exercise4():
	total = 0
	for number in range(1,101,2):
		total += number
	print(total)

def exercise5():
	for num in range(1, 101):
		if num % 3 == 0 and num % 5 == 0:
			print("Fizz Buzz")
		elif num % 3 == 0:
			print("Fizz")
		elif num % 5 == 0:
			print("Buzz")
		else:
			print(num)

import random

def project1():
	letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

	print("Welcome to the PyPassword Generator!")
	nr_letters = int(input("How many letters would you like in your password?\n")) 
	nr_symbols = int(input(f"How many symbols would you like?\n"))
	nr_numbers = int(input(f"How many number would you like?\n"))

	# Easy Level

	# password = ""

	# for char in range(1, nr_letters + 1):
	# 	password += random.choice(letters)

	# for char in range(1, nr_symbols + 1):
	# 	password += random.choice(symbols)

	# for char in range(1, nr_numbers + 1):
	# 	password += random.choice(numbers)

	# print(password)

	# Hard Level
	# g^2jk8&

	password_list = []

	for char in range(1, nr_letters + 1):
		password_list += random.choice(letters)

	for char in range(1, nr_symbols + 1):
		password_list += random.choice(symbols)

	for char in range(1, nr_numbers + 1):
		password_list += random.choice(numbers)

	print(password_list)
	random.shuffle(password_list)
	print(password_list)

	password = ""
	for char in password_list:
		password += char
	print(f"Your password is: {password}")
