import math


def greet():
	print("Hello")
	print("How do you do?")
	print("Isn't the weather nice today?")

def greet_with_name(name):
	print(f"Hello {name}")
	print(f"How do you do {name}?")
	print("Isn't the weather nice today?")

def greet_with(name, location):
	print(f"Hello {name}")
	print(f"What is it like in {location}")
	
def paint_calc(height, width, cover):
	area = height * width
	num_of_cans = math.ceil(area/cover)
	print(f"You'll need {num_of_cans} cans of paint")


def prime_checker(number):
	is_prime = True
	for i in range(2, number):
		if number % i == 0:
			is_prime = False
	if is_prime:
		print("It's a prime number.")
	else:
		print("It's not a prime number")
	# is a prime

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# def encrypt(plain_text, shift_amount):
# 	cipher_text = ""
# 	for letter in plain_text:
# 		current_index = alphabet.index(letter)
# 		new_index = (current_index + shift_amount) % 26
# 		cipher_text += alphabet[new_index]
# 	print(f"The encoded text is {cipher_text}")

# def decrypt(cipher_text, shift_amount):
# 	plain_text = ""
# 	for letter in cipher_text:
# 		current_index = alphabet.index(letter)
# 		new_index = (current_index - shift_amount) % 26
# 		plain_text += alphabet[new_index]
# 	print(f"The encoded text is {plain_text}")

def caesar(start_text, shift_amount, cipher_direction):
	end_text = ""
	if cipher_direction == "decode":
		shift_amount *= -1
	for char in start_text:
		if char in alphabet:
			current_index = alphabet.index(char)
			new_index = current_index + shift_amount
			end_text += alphabet[new_index]
	print(f"Here's the {cipher_direction}d result: {end_text}")
