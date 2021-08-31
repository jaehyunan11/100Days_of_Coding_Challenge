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

def test3():
	fruits = ["strawberries"]
	vegtables = ["Spinach"]
	dirty_dozen = [fruits, vegtables]
	print(dirty_dozen)