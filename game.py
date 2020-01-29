import random

def PlayGame():

    user_choice = (input("Please choose either 'rock', 'paper', or 'scissors':  "))
    while (user_choice.lower() != "rock" and user_choice.lower() != "paper" and user_choice.lower() != "scissors") :
        print("Try again")
        user_choice = (input("Please choose either 'rock', 'paper', or 'scissors':  "))
    print("You chose: " + user_choice)
    return user_choice.lower()
    


def WholeGame(option, lists):

    computer_choice = random.choice(lists)
    print("The computer chose " + computer_choice + " ")
    print("-------------------")
    tie_flag = True
    retry = False
    while(tie_flag == True):




        ### This was originally supposed to be a case for if there was a retry for the game ###


       #if retry == True:
       #    #retry = False
       #    newOption = PlayGame() #
       #    if (WholeGame(newOption, lists) == True):
       #        quit()

        #else:
        if computer_choice == option:
            print("Tie play again")
            tie_flag = False
            #retry = True
    
    
        elif (computer_choice == "scissors" and option == "paper") :
            print("Oh, the computer won. It's ok.")
            tie_flag = False
            #print(retry)
            #retry = True
        elif (computer_choice == "rock" and option== "scissors"):
            print("Oh, the computer won. It's ok." )
            tie_flag = False
            #print(retry)
            #retry = True
        elif (computer_choice == "paper" and option == "rock"):
            print ("Oh, the computer won. It's ok." )
            tie_flag = False
            #print(retry)
            #retry = True
        else:
            print("You win!")
            tie_flag = False
            #return True
        
        print("-------------------")
        print("Thanks for playing. Please play again!\n")
    

            
choices = ["rock", "paper", "scissors"]

print("\n-------------------")
print("Welcome to my Rock-Paper-Scissors game...")
print("-------------------")

#print("You chose: ",)
option = PlayGame()
WholeGame(option, choices)

#-------------------
#Welcome to my Rock-Paper-Scissors game...
#-------------------
#Please choose either 'rock', 'paper', or 'scissors': rock
#You chose: 'rock'
#The computer chose: 'paper'
#-------------------
#Oh, the computer won. It's ok.
#-------------------
#Thanks for playing. Please play again!