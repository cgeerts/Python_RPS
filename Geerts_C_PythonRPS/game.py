# import the random package so that we can generate a random choice

from random import randint
from gameFunctions import winlose, functions

#nets options
choices = ["rock", "paper", "scissors"]

#set up some variables for player and AI lives

functions.player_lives = 5
functions.computer_lives = 5

#let the AI make a choice

functions.computer = choices[randint (0,2)]

player = False

# choices is an array => an array is a container that can hold multiple values
# arrays are 0-based -> first entry is 0, 2nd is `, 3rd is 2 etc

choices = ["rock", "paper", "scissors"]

# set the functions.computer variable to one of these choices

functions.computer = choices[randint(0, 2)]

# set up the game loop so that we don't have to restart all the time

player = False

while functions.player == False:

	#set player to True
	print("==<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>==")
	print("Computer lives:", functions.computer_lives, "/", functions.total_lives)
	print("Player lives:", functions.player_lives, "/", functions.total_lives)
	print("==<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>==")
	print("Choose your weapon!\n")

	player = input("choose rock, paper or scissors: \n")
	player = player.lower()

	print("The computer chose", functions.computer, "\n")
	print("The player chose", functions.player, "\n")

	#handle all lives lost for player or AI

	if functions.player_lives is 0:
		winlose.winorlose("lost")
#
#		print("You lost all lives! Would you like to play again?")
#		choice = input("Y / N")
#		print (choice)
#
#		if (choice is "Y") or (choice is "y"):
#			print("You chose to quit.")
#
#			exit()
#
#		elif (choice is "N") or (choice is "n"):
#			player_lives = 5
#			player = False
#			
	elif functions.computer_lives is 0:
		winlose.winorlose("win")

#		print("functions.Computer is out of lives! You rock at this game. Would you like to play again?")
#		choice = input("Y / N")
#
#		if (choice is "N") or (choice is "n"):
#			print("You chose to quit.")
#			exit()
#
#		elif (choice is "Y") or (choice is "y"):
#			#reset the game and start over again
#		
#			player_lives = 5
#			functions.computer_lives = 5
#			player = False
#			functions.computer = choices[randint(0,2)]
#
#	else:
#		# need to check all of our conditions after checking for a tie
#
	player = False
	functions.computer = choices[randint(0, 2)]