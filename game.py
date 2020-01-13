import random

def PlayGame():

    user_choice = (input("Enter Rock, Paper, or Scissors   "))
    while (user_choice.lower() != "rock" and user_choice.lower() != "paper" and user_choice.lower() != "scissors") :
        print("Try again")
        user_choice = (input("Enter Rock, Paper, or Scissors   "))
    print("You chose " + user_choice)
    return user_choice.lower()
    


def WholeGame(option, lists):

    computer_choice = random.choice(lists)
    print("Your opponent chose " + computer_choice + " ")
    tie_flag = True
    retry = False
    while(tie_flag == True):

        if retry == True:
            retry = False
            newOption = PlayGame()
            WholeGame(newOption, lists)
        if computer_choice == option:
            print("Tie play again")
            newOption = PlayGame()
            WholeGame(newOption,lists)
        
        
        elif (computer_choice == "scissors" and option == "paper") :
            retry = input("Sorry you lost your opponent chose " + computer_choice+" press any key to continue playing" )
            print(retry)
            retry = True
        elif (computer_choice == "rock" and option== "scissors"):
            retry = input("Sorry you lost your opponent chose " + computer_choice+" press any key to continue playing" )
            print(retry)
            retry = True
        elif (computer_choice == "paper" and option == "rock"):
            retry = input("Sorry you lost your opponent chose " + computer_choice+" press any key to continue playing" )
            print(retry)
            retry = True
        else:
            print("You win!")
            tie_flag = False
    

            
choices = ["rock", "paper", "scissors"]
print("This game is called Rock, Paper, Scissors, Shoot!")
option = PlayGame()
WholeGame(option, choices)