import random

play = True

optiondict = {
    "rock":  1,
    "paper": 2,
    "scissors": 3
}

while play == True:

    #Input user decision
    choice = input("Choose Rock, Paper or Scissors respectively  > ")
    choice = choice.lower()     #so input it not case sensitive

    if choice not in optiondict:
        print("Input is invalid, please type either Rock, Paper, Scissors")
        continue    
    else:
        choice = optiondict[choice]
        
        #Generate computer decision
        opchoice = (random.randint(1, 3))

        #reverses dictionary 
        print("Your opponent played", list(optiondict.keys())
            [list(optiondict.values()).index(opchoice)])

        #calculates who won
        if choice - opchoice == 0:
            print("Draw! The same choice!")
        elif choice - opchoice == 1 or choice - opchoice == -2:
            print("You win")
        else:
            print("You lose")

    playagain = input("Type 1 to play again, 2 to exit > ")
    if playagain == 2:
        play == False