from random import randint
from RPS_art import rock, paper, scissors
rps_list = ["rock", "paper", "scissors"]
end_of_game = False
print("Welcome to the game.")
while not end_of_game:
	player=input("Rock, Paper or Scissors?\n").lower()
	if player == rps_list[2]:
		player = scissors
	elif player == rps_list[0]:
		player = rock
	elif player == rps_list[1]:
		player = paper
	else:
		print("Invalid input!")
		print("---")
		print("Rock, Paper or Scissors?")
		player=input()
	print("---")
	print("Player choose: " + player)
	computer=randint(0,2)
	if computer == 0:
		computer = rock
	if computer == 1:
		computer = paper
	if computer == 2: 
		computer = scissors
	print("computer choose: " + computer)
	print("---")
	if player == computer:
		print("Draw")
	else:	
		if player == rock:
			if computer == paper:
				print("Rock < Paper, Computer win")
			else:
				print("Rock > Scissors, Player win")		
		elif player == paper:
			if computer == scissors:
				print("Paper < Scissors, Computer win")
			else: 
				print("Paper > Rock, Player win")
		elif player == scissors:
			if computer == rock:
				print("Scissors < Rock, Computer win")
			else: 
				print("Scissors > Paper, Player win")
	if input("Do you want a rematch? (Y/N)").upper() !="Y":
		end_of_game = True

print("Bye!")