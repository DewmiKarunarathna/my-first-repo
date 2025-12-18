#choose your own adventure game
import time
def show_title():
    print_slow(r"""
     _    _      _                           
    | |  | |    | |                          
    | |  | | ___| | ___ ___  _ __ ___   ___  
    | |/\| |/ _ \ |/ __/ _ \| '_ ` _ \ / _ \ 
    \  /\  /  __/ | (_| (_) | | | | | |  __/ 
     \/  \/ \___|_|\___\___/|_| |_| |_|\___| 
    """)
    print_slow("🎮 YOUR ADVENTURE BEGINS... 🎮")
#start
def start_adventure():
    print("🌲🌲🌲Forest Adventure🌲🌲🌲")
    print("You wake up in a mysterious forest 🫢")
    choice = input("NORTH or SOUTH?").lower() #translate the input in to lowercase
    if choice=="north":
        print("You are entering to a cave 😯")
        cave_choice = input("Would you walk into the cave? 🤯 y/n").lower()
        if cave_choice == ["y", "yes"]:
            #
        else :
            #
    else:
        print("You find a river 😯")
        #continue
def turn():
    choice = input("Which way you want to go ? Left or right? 🤔").lower()
def cave_in():
    print("The cave is getting darker 😨")
    print("Press 1 to search for a light in the backpack")
    print("Press 2 to light a fire ")
    choice = int(input("Your choice : ")
    if choice == 1:
        #
    elif choice == 2:
        #
    else:
                 
                 
                 
    
