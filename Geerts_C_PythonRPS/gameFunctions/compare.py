from gameFunctions import functions

#need a function to run to compate the choices
#figure out what to pass into the function

def compareChoices():

		if player.lower() == "quit":
		exit()

	elif functions.computer == player:
		print("tie! no one wins, play again")

	elif player.lower() == "rock":

		if functions.computer == "paper":
			print("You lose!", functions.computer, "covers", player, "\n")
			player_lives = player_lives - 1

		else:
			print("You win!", player, "smashes", functions.computer, "\n")
			functions.computer_lives = functions.computer_lives - 1

	elif player.lower() == "paper":

		if functions.computer == "scissors":
			print("You lose!", functions.computer, "cuts", player, "\n")
			player_lives = player_lives - 1

		else:
			print("You win!", player, "covers", functions.computer, "\n")
			functions.computer_lives = functions.computer_lives - 1

	elif player.lower() == "scissors":

		if functions.computer == "rock":
			print("You lose!", functions.computer, "smashes", player, "\n")
			player_lives = player_lives - 1

		else:
			print("You win!", player, "cuts", functions.computer, "\n")
			functions.computer_lives = functions.computer_lives - 1

	else:
		print("thats not a valid choice, try again")