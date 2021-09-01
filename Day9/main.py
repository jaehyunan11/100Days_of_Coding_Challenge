def test1():
	programming_dictionary = {
		"Bug": "An error in a program that prevents the program from running as expected.",
		"Function": "A piece of code that you can easily call over and over again.",
		"Loop": "The action of doing something over and over again.",
	}

	# print(programming_dictionary["Function"])

	# programming_dictionary["Loop"] = "The action of doing something over and over again."

	# print(programming_dictionary)

	# # Creating an empty dictionary
	# empty_dictionary = {}

	# # Wipe an existing dictionary
	# programming_dictionary = {}
	# print(programming_dictionary)

	# Edit and item in a dictionary
	# programming_dictionary["Bug"] = "A moth in your computer."
	# print(programming_dictionary)

	# Loop the dictionary

	for key in programming_dictionary:
		print(key)
		print(programming_dictionary[key])

def exercise1():
	student_scores = {
		"Harry": 81,
		"Ron": 78,
		"Hermione": 99,
		"Draco": 74,
		"Neville": 62
	}

	# TODO-1 : Create an empty dictionary called student_grades
	student_grades = {}

	#TODO-2 : Write your code below to add the greades to 

	for student in student_scores:
		score = student_scores[student]
		if score > 90:
			student_grades[student] = "Outstanding"
		elif score > 80:
			student_grades[student] = "Exceeds Expectations"
		elif score > 70:
			student_grades[student] = "Acceptable"
		else:
			student_grades[student] = "Fail"

	print(student_grades)


def test2():
	# Nesting
	capitals = {
		"France": "Paris",
		"Germany": "Berlin",
	}

	# Nesting a List in a Dictionary

	travel_log = {
		"France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
		"Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
	}

	# Nesting Dictionary in a Dictionary


	travel_log = {
		"France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
		"Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
	}

	# Nesteing Dictionary in a list

	travel_log = {
		{"country": "France", 
		"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12
		},
		{"country": "Germany",
		"cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
		"total_visits": 5
		}
	}

travel_log = [
	{
		"country": "France",
		"visits": 12,
		"cities": ["Paris", "Lille", "Dijon"]
	},
	{
		"country": "Germany",
		"visits": 5,
		"cities": ["Berlin", "Hamburg", "Stuttgart"]
	},
]

def add_new_country(country_visited, time_visited, cities_visited):
	new_country = {}
	new_country["Country"] = country_visited
	new_country["visits"] = time_visited
	new_country["cities"] = cities_visited
	travel_log.append(new_country)
	print(travel_log)


from Day9 import logo
from replit import clear

def project1():
	print(logo.logo)

	bids = {}
	bidding_finished = False

	def find_highest_bidder(bidding_record):
		# bidding_record = {"Jaehyun": 123, "James": 321}
		highest_bid = 0
		for bidder in bidding_record:
			bid_amount = bidding_record[bidder]
			if bid_amount > highest_bid:
				highest_bid = bid_amount
				winner = bidder
		print(f"bids:\n{bids}")
		print(f"The winner is {winner} with a bid of ${highest_bid}")

	while not bidding_finished:
		name = input("What is your name?\n")
		price = int(input("What is your bid?\n$"))
		bids[name] = price

		should_continue = input("Are there any other bidders? Type 'yes' or 'no' ").lower()
		if should_continue == "no":
			bidding_finished = True
			find_highest_bidder(bids)
		elif should_continue == "yes":
			clear()

	