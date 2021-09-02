# print("Day 1 - Python Print Function")
# print("The function is declared like this:")
# print("print('what to print')")
# print("Hello World!\nHello WOrld!\nHello World!")
# print("Hello" + " " + "Jaehyun")
# print("Hello " + "Jaehyun")
# print("Hello" + " Jaehyun")

# fix the code below
# print("Day1 - String manipulation")
# print("String Concatenation is done with the "'+'" sign.")
# print('e.g. print("Hello" + "world")')
# print("New lines can be createddwith a backslash and n.")

# input function
# input() will getduser input in console
# Then print() will print the world "Hello" and the user input
# print("Hello" + input("What is your name?"))

# Write your code belw this line

# print(len("Jaehyun"))
# print(len(input ("What is your name?")))

# name = input("What is your name?")
# length = len(name)
# print(length)

# Don't change the code below
# a = input("a:")
# b = input("b:")

# # Write your code below this line
# c = a
# a = b
# b = c

# #1. Create a greeting for your porgram
# print("Welcome to the band name generator.")
# #2 Ask the user for the city that they grew up in
# city = input("Which city did you grow up in?\n")
# #3 Ask the user for the name of a pet
# pet = input("What is the name of a pet?\n")
# #4 Combine the name of their city and pet and show them their band name
# print("Your band name could be " + city + " " + pet)
# #5 Make sure the input cursor shows on a new line, 
# # put \n 

# from Day2 import main

# m = main

# main.first()
# main.test1()
# main.test2()
# m.test3()
# m.exercise1()
# m.test4()
# m.exercise2()
# m.test5()
# m.exercise3()
# m.exercise4()


# from Day3 import main

# m = main

# m.test1()
# m.exercise1()
# m.test2()
# m.exercise2()
# m.exercise3()
# m.exercise4()
# m.exercise5()
# m.exercise6()
# m.exercise7()
# m.project1()

# from Day4 import main

# m = main

# m.test1()
# m.exercise1()
# m.test2()
# m.exercise2()
# m.exercise3()
# m.project1()

# from Day5 import main

# m = main

# m.test1()
# m.exercise1()
# m.exercise2()
# m.test2()
# m.exercise3()
# m.exercise4()
# m.exercise5()
# m.project1()

# from Day6 import main

# m = main

# m.my_function()


# from Day7 import main

# m = main

# m.exercise1()

# from Day8 import main

# m = main

# m.greet()
# print("\n")
# m.greet_with_name("Jaehyun")
# print("\n")
# m.greet_with(name="Jaehyun", location="Fremont")

# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# m.paint_calc(height=test_h, width=test_w, cover=coverage)

# n = int(input("Check this number: "))
# m.prime_checker(number=n)


# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

# m.caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

# from Day8 import art

# print(art.logo)

# should_end = False
# while not should_end:
# 	direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# 	text = input("Type your message:\n").lower()
# 	shift = int(input("Type the shift number:\n"))

# 	shift = shift % 26

# 	m.caesar(start_text=text, shift_amount= shift, cipher_direction=direction)

# 	restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'. \n")
# 	if restart == 'no':
# 		should_end = True
# 		print("GoodBye")


# from Day9 import main

# m = main

# m.test1()
# m.exercise1()
# m.add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# m.project1()


# from Day10 import main, logo

# m = main

# m.format_name(input("What is your first name?\n"), input("What is your last name?\n"))

# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = m.days_in_month(year, month)
# print(days)

# m.format_name()
# m.project1()

from Day11 import main

m = main
m.play_game()