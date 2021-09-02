# Functions with Outputs

def format_name(f_name, l_name):
	"""Take a first and last name and format it to return the title case version of the name. 
	"""
	if f_name == "" or l_name == "":
		return "You didn't provide valid inputs"

	formated_f_name = f_name.title()
	formated_l_name = l_name.title()

	return (f"Result: {formated_f_name} {formated_l_name}")
def is_leap(year):
	if year % 4 == 0:
		if year % 100 == 0:
			if year % 400 == 0:
				return True
			else:
				return False
		else:
			return True
	else:
		return False

def days_in_month(year, month):
	if month > 12 or month < 1:
		return "Invalid month"
	month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
	if is_leap(year) and month == 2:
		return 29
	return month_days[month - 1]

from Day10 import logo

def project1():
	# Calculator

	# Add
	def add(n1,n2):
		return n1 + n2

	# Subtract
	def subtract(n1,n2):
		return n1 - n2

	# Multiply
	def multiply(n1, n2):
		return n1 * n2

	# Divide
	def divide(n1, n2):
		return n1 / n2

	operations = {
		"+": add,
		"-": subtract,
		"*": multiply,
		"/": divide,
	}

	print(logo.logo)

	num1 = float(input("What's the first number?:\n"))
	for symbol in operations:
		print(symbol)

	should_continue = True

	while should_continue:
		operation_symbol = input("Pick an operation:\n")
		num2 = float(input("What's the next number?:\n"))
		calculation_function = operations[operation_symbol]
		answer = calculation_function(num1, num2)

		print(f"{num1} {operation_symbol} {num2} = {answer}")

		if input(f"Type 'y' to continue caluclating with {answer}, or type 'n' to start a new calculation:\n") == "y":
			num1 = answer
		else:
			should_continue = False



		


