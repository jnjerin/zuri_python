#Rock-Paper-Scissors game
#Create the different options
#Ask the user to pick an option between "R", "P" or "S"
#If user input is invalid (not amongst our options), print an error, and ask for their input again
#Use the `choice` function from the inbuilt Python `random` module to make a choice for CPU player(computer).
#Print both player's moves in the format: `Player (Rock) : CPU (Paper)`
#Check both player's moves: 
#If there is a winner, print the winner, and the program ends. 
#If it's a tie (the computer and player pick the same move), restart the game

#import random module to make a choice for CPU player
from multiprocessing import RLock
import random

#while statement:ask player if they want to play again after each round. break at the end to quit the game

choices = ["rock","paper","scissors"]

computer = random.choice(choices)
player = None
#take user input and make it lower case with .lower() method
#only take user input that's within the choices
while player not in choices:
    player = input("rock, paper, or scissors?: ").lower() 

#check if computer choice matches player choice and print "tie"
if player == computer:
    print("player (",player + " )" " : " + "computer (",computer + " )" )
    print("You tie! Continue playing")
    player = input("rock, paper, or scissors?: ").lower() 

#If player chooses rock while computer chooses paper, player loses.Player wins if computer chooses scissors
elif player == "rock":
    if computer == "paper":
        print("player (",player + " )" " : " + "computer (",computer + " )" )
        print("---GAME OVER!! Computer wins.You lost!")
    
    if computer == "scissors":
        print("player (",player + " )" " : " + "computer (",computer + " )" )
        print("Congratulations!! You are the winner! ---GAME OVER!!--- ")

#If player chooses scissors while computer chooses rock, player loses.Player wins if computer chooses paper
elif player == "scissors":
    if computer == "rock":
        print("player (",player + " )" " : " + "computer (",computer + " )" )
        print("---GAME OVER!! Computer wins.You lost!")
    if computer == "paper":
        print("player (",player + " )" " : " + "computer (",computer + " )" )
        print("Congratulations!! You are the winner! ---GAME OVER!!--- ")

#If player chooses paper while computer chooses scissors, player loses.Player wins if computer chooses rock
elif player == "paper":
    if computer == "scissors":
        print("player (",player + " )" " : " + "computer (",computer + " )" )
        print("---GAME OVER!! Computer wins.You lost!")
    if computer == "rock":
        print("player (",player + " )" " : " + "computer (",computer + " )" )
        print("Congratulations!! You are the winner! ---GAME OVER!!--- ")
        

