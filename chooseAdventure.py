#choose your own adventure game
import time
def print_slow(text, delay = 0.33):
    """Print text with a typewriter effect"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()
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
            cave_in()
        else :
            print("You decided to not to go in the cave, you turn arount and you see a glowing path")
            print("🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟")
            glow()
    else:
        print("You find a river 😯")
        river()
def turn():
    choice = input("Which way you want to go ? Left or right? 🤔").lower()
def cave_in():
    print("The cave is getting darker 😨")
    print("Press 1 to search for a light in the backpack")
    print("Press 2 to light a fire ")
    choice = int(input("Your choice : ")
    if choice == 1:
        print("You have found a torch 🔦")
    elif choice == 2:
        print("You light a fire 🔥")
    else:
def river():
def glowing_path():
    print("\n✨✨✨ The Glowing Path ✨✨✨")
    print("The path shimmers with magical energy!")
    print("It leads to two different areas:")
    print("1. An ancient temple 🏛️")
    print("2. A hidden village 🏘️")    
    while True:
        try:
            choice = int(input("Where do you go? (1/2) : "))
            if choice == 1:
                ancient_temple()
                break
            elif choice == 2:
                hidden_village()
                break
            else:
                print("Please enter 1 or 2")
        except:
            print("Enter a number")
    
