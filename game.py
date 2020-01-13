import random
choices = ["rock", "paper", "scizzors"]

print("This game is called Rock, Paper, Scizzors, Shoot!")
user_choice = (input("Enter Rock, Paper, or Scizzors")
while user_choice.lower() != "rock" and user_choice.lower() != "paper" and user_choice.lower() != "scizzors":
    print("Try again")
    user_choice = (input("Enter Rock, Paper, or Scizzors")
print("You chose " + user_choice)

computer_choice = random.choice(choices)
print("Your opponent chose " + computer_choice)
tie_flag = True

while(tie_flag == True):

    if (computer_choice.lower() == user_choice):
        print("Tie play again")
        
    elif (computer_choice.lower() == "rock" and user_choice.lower() == "paper") :
        retry = input("Sorry you lost press any key to continue playing") 
    elif (computer_choice.lower() == "paper" and user_choice.lower()== "scizzors"):
        retry = input("Sorry you lost press any key to continue playing")
    elif (computer_choice.lower() == "scizzors" and user_choice.lower()== "rock"):
        retry = input("Sorry you lost press any key to continue playing")
    else:
        "You win!"
        tie_flag = False
    

            
    
