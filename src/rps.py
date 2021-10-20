import random

#Game outcomes
outcomes = {
    "rock":{"rock":"draw","paper":"loss","scissors":"win"},
    "paper":{"rock":"win","paper":"draw","scissors":"loss"},
    "scissors":{"rock":"loss","paper":"win","scissors":"draw"}
}


def converted_outcome(number):
    if number == 1:
        return "rock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "scissors"

#Main loop 
while 1:
    random_number = random.randint(1,3)
    computer_choice = converted_outcome(random_number)
    user_choice   = input(str("Select rock/paper/scissors : "))
    try:
        print("You selected : ",user_choice)
        print("The Computer selected : ",computer_choice)
        print(" *** Game outcome *** ")
        print(outcomes[user_choice][computer_choice])
        print("")
    except:
        print("invalid Input!!")
