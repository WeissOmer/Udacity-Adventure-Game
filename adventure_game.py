import time
import random
items = []
places = ["Supermarket", "Car Wash", "Police Station", "Post Office"]


def print_pause(message):
    time.sleep(2)
    print(message)
    time.sleep(2)


def intro():
    print_pause("You are in desert, the sun is almost out."
                "in your hand you are holding a screwdriver.")
    print_pause("There is smoke coming out of your car, it's clearly broken")
    print_pause("To your north you see some lights, it's a village!\n")


def fixing_car():
    if "gas" in items:
        print_pause("You put gas in the tank")
        print_pause("You are turning the engine on and.....")
        print_pause("It's working!! the jeep is fixed!! you won!!")
        choice = input("Do you want to play again?\n"
                       "Please enter the 1 or 2 to choose\n\n"
                       "1. Play again\n" "2. Exit\n")
        while True:
            if choice == "1":
                items.remove("gas")
                play_game()
            elif choice == "2":
                quit()
            else:
                choice = input("Do you want to play again?\n"
                               "Please enter the 1 or 2 to choose\n\n"
                               "1. Play again\n" "2. Exit\n")
    else:
        print_pause("You you are trying to fix the car with the screwdriver,"
                    "but mmm... that doesn't seems to work\n")
        player_choice()


def village_Intro():
    place = random.choice(places)
    print_pause("You got into the village,"
                "infront of you there is a " + place + ".")
    print_pause("Do you want to go in?\n")


def village():
    time.sleep(2)
    choice = input("What would you like to do?\n"
                   "Please enter the 1 or 2 to choose\n\n"
                   "1. Continue looking in the village\n"
                   "2. Go in\n")
    if choice == "1":
        print_pause("Mmmm... it doesn't seems like there is anything else here")
        village()
    elif choice == "2":
        print_pause("The place is happy to give you gas to try!")
        items.append("gas")
        player_choice()
    else:
        village()


def player_choice():
    print_pause("What would you want to do?\n"
                "Please enter 1 or 2 to choose\n")
    choice = input("1. Try to fix the car\n"
                   "2. Go to the village\n")
    if choice == "1":
        fixing_car()
    elif choice == "2":
        if "gas" in items:
            print_pause("Mmmm... it doesn't seem like there"
                        "is anything else here")
            player_choice()
        else:
            village_Intro()
            village()
    else:
        player_choice()


def play_game():
    intro()
    player_choice()


play_game()
