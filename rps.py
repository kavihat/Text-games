
import random
option=['Rock', 'Paper', 'Scissors']
print("*******ROCK, PAPER and SCISSORS********")

rounds=int(input("Howmany rounds do you want?"))
print(rounds)
cscore=0
pscore=0
while(rounds):
    i = random.randint(0, 2)
    players_input = (input('Enter your input : ')).upper()
    computer_input=option[i].upper()
    print("Computer's input : " +computer_input)
    rounds = rounds - 1
    if (computer_input == players_input):
        print("its a draw!,no one get points")
    elif (players_input == 'ROCK' and computer_input == 'PAPER'):
        print("Computer gets a point")
        cscore=cscore+1
    elif (players_input == 'ROCK' and computer_input == 'SCISSORS'):
        print("Player gets a point")
        pscore=pscore+1
    elif (players_input == 'PAPER' and computer_input == 'SCISSORS'):
        print("Computer gets a point")
        cscore=cscore+1
    elif (players_input == 'PAPER' and computer_input == 'ROCK'):
        print("Player gets a point")
        pscore=pscore+1
    elif (players_input == 'SCISSORS' and computer_input == 'ROCK'):
        print("Computer gets a point")
        cscore=cscore+1
    elif (players_input == 'SCISSORS' and computer_input == 'PAPER'):
        print("Player gets a point")
        pscore=pscore+1
if(cscore==pscore):
    print("its a draw match")
elif(cscore>pscore):
    print("Computer wins")
else:
    print("player wins")


