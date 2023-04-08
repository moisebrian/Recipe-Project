#!/usr/bin/env python3

import math
groundbeef = 4 # 4 serving in one pack of ground beef
burgerBuns = 8 # 8 buns in one pack
a_cheese = 24  # 24 slices of american cheese in one pack

people = int(input("How many people are attending the cookout? :"))
burgerperperson = int(input("\nHow many burgers will each person eat?: "))
cheesepeople = int(input("How many people want cheese on their burgers?: "))

patties_required = (people * burgerperperson)/groundbeef
patties_needed = math.ceil(patties_required)

buns_required =(people * burgerperperson)/burgerBuns
buns_needed = math.ceil(buns_required)

cheese_required = (cheesepeople * burgerperperson) / a_cheese
cheese_needed = math.ceil(cheese_required)

leftover_buns = (buns_needed * burgerBuns) - (people * burgerperperson)
leftover_patties = (patties_needed * groundbeef) - (people * burgerperperson)
leftover_cheese = (cheese_needed * a_cheese) - (cheesepeople * burgerperperson)


if cheesepeople > people:
	print("Invalid entry. Please try again.")
else:
	print("\nThe minimum number of packages of ground beef required: ",patties_needed)

	print()
	print("The minimum number of packages of burger buns required: ", buns_needed)
	
	print()
	print("The minimum number of packages of cheese required: ",cheese_needed)
	
	print()
	print("The number of patties that will be left over: ", leftover_patties)

	print()
	print("The number of cheese slices that will be left over: ", leftover_cheese)
	print()
	print("The number of burger buns that will be left over: ",leftover_buns)