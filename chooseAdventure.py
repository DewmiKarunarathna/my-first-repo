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
        cave_choice = input("Would you walk into the cave? 🤯")
        #continue
    else:
        print("You find a river 😯")
        #continue
