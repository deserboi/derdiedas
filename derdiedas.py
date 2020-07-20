### DER, DIE, DAS? ###

import requests as r
from bs4 import BeautifulSoup as bs
import time
import random
import os

used_words = []
word = ""
all_words_used = False

print("""	\n	  Welcome to DER, DIE, DAS?
A little game to train your knowledge on Artikeln in german :)

			-t
""")

def game():

	global used_words, word, all_words_used

	with open("words.txt", "r") as f:
		contents = f.read().split()
		print("--------------------------------------------------------------")
		print("Loaded words...")
		print("Total words in txt file: ", len(contents), "\n")
		
		tri = 0
		word = random.choice(contents)
		if word in used_words:
			while word in used_words:
				word = random.choice(contents)
		
				if tri == 15: # something wrong here smh
					print("Already used all words :( , please put new words in txt file.\n")
					print("Exiting program...")
					all_words_used = True
					break
		else:
			print(f"Your word is: {word}")
			ans = input("Please type the correct artikel for the word and press enter: > ")
			ans = ans.strip()
			ans = ans[0:3]
			gotem = r.get(f"https://www.duden.de/rechtschreibung/{word}")
			bsget = bs(gotem.text, "lxml")
			artikel = str(bsget.find("span", {"class": "lemma__determiner"}).text)

			if ans == artikel:
				print(f"\nCorrect! The answer is {artikel} {word}")
				used_words.append(word)
				tri += 1
			elif ans != artikel:
				print(f"\nWrong! The correct artikel is {artikel}, so {artikel} {word}")

			
game()
round = 2

while True:
	if all_words_used == True:
		break
	else:
		q = str(input("\nAnother round? (y/n): > ").lower())
		q = q.strip()
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
			print("\nInvalid input :(")
			time.sleep(1)
			pass
