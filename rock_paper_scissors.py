import random


#Input user decision
choice = input("Choose Rock, Paper or Scissors respectively > ")

optiondict = {
    "Rock":  "1",
    "Paper": "2",
    "Scissors": "3"
}

if (choice != "Rock" and choice != "Paper" and choice != "Scissors" and choice != "rock" and choice != "paper" and choice != "scissors"):
    print("Input is invalid, please select either Rock, Paper, Scissors")
    exit()
else:
    choice = int(optiondict[choice])

#Generate computer decision
opchoice = str((random.randint(1, 3)) )

#reverses dictionary 
print("Your opponent played", list(optiondict.keys())
      [list(optiondict.values()).index(opchoice)])

opchoice = int(opchoice)

#calculates who won
if choice - opchoice == 0:
    print("Draw! The same choice!")
elif choice - opchoice == 1 or choice - opchoice == -2:
    print("You win")
else:
    print("You lose")