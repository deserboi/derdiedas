### DER, DIE, DAS? ###

import requests as r
from bs4 import BeautifulSoup as bs
import time
import random
import os


print("""	\n	  Welcome to DER, DIE, DAS?
A little game to train your knowledge on Artikeln in german :)

			-t
""")

def game():

	with open("words.txt", "r") as f:
		contents = f.read().split()
		print("--------------------------------------------------------------")
		print("Loaded words...")
		print("Total words in txt file: ", len(contents), "\n")
		word = random.choice(contents)

	print(f"Your word is: {word}")
	ans = input("Please type the correct artikel for the word and press enter: > ")

	gotem = r.get(f"https://www.duden.de/rechtschreibung/{word}")
	bsget = bs(gotem.text, "lxml")
	artikel = str(bsget.find("span", {"class": "lemma__determiner"}).text)


	if ans == artikel:
		print(f"\nCorrect! The answer is {artikel} {word}")
	elif ans != artikel:
		print(f"\nWrong! The correct artikel is {artikel}, so {artikel} {word}")


game()
round = 2

while True:
	q = str(input("\nWould you like to play again? (y/n): > \n").lower())
	time.sleep(1)
	if q == "y":
		print(f"Alright, going for round {round}!\n")
		time.sleep(2)
		os.system("cls")
		game()
		round += 1
	elif q == "n":
		print("\nSee you next time!")
		break
	else:
		print("Invalid input :(")
		print("Quitting program...")
		time.sleep(1)
		break