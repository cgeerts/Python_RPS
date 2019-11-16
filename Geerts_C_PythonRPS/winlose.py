from random import randint
from gameFunctions import functions

def winorlose(status):
	print("called win or lose", status)
	print("You", status, "! Would you like to play again?")
	choice = input("Y / N?")

	if choice == "Y" or choice == "y":
		global player_lives
		global computer_lives
		global player
		global computer

	#reset the game and start all over again
	
	functions.player_lives = 5
	functions.computer_lives = 5
	functions.player = False
	functions.computer = functions.choices[randint (0,2)]

elif choice == "N" or choice == "n":
	print("You chose to quit. Better luck next time.")
	exit()

else:
	print("Make a valid input. Yes or no.")

#recursion (calling a function from inside itself)

	winorlose(status)