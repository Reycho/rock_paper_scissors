import random

#Input user decision
choice = input("Choose 1, 2, 3, rock paper sissors respectively ")
if (choice != "1" and choice != "2" and choice != "3"):
    print("Input invalid")
    exit()
else:
    choice = int(choice)

#Generate computer decision
opchoice = (random.randint(1, 3)) 

if choice - opchoice == 0:
    print("Draw! The same choice!")#
elif choice - opchoice == 1 or choice - opchoice == -2:
    print("You win")
else:
    print("You lose")