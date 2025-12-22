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
            door()
            
        else :
            print("You decided to not to go in the cave, you turn arount and you see a glowing path")
            print("🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟")
            glowing_path()
    else:
        print("You find a river 😯")
        river()
def turn():
    choice = input("Which way you want to go ? Left or right? 🤔").lower()
    return choice
def cave_in():
    print("The cave is getting darker 😨")
    print("Press 1 to search for a light in the backpack")
    print("Press 2 to light a fire ")
    choice = int(input("Your choice : ")
    if choice == 1
        print("You have found a torch 🔦")
    elif choice == 2:
        print("You light a fire 🔥")
    else:
def game_to_boat():
    print("You have to correctly identify all 4 numbers in the lock 🔒")
    print("First number is rhymes with tree 🌴")
    print("Second number comes from (3y +5)3/2 = 21")
    print("Last digits are the addition of first two digits times 2")
    answer = input("Your answer is : ").lower()
    if answer == "3312":
        return True
    else:
        return False
def door():
    print("You see two doors leading left and right")
    turn()
    if turn()=="left":
        cave_out()
    elif turn()=="right":
        trap()
    else:
        print("Invalid input")
def river():
    print("You are seeing a river, to get to the other side, you need to get a boat")
    print("You have to open a lock to open the gate to get the boat ⛵")
    game_to_boat()   
def ancient_temple():
    print("This temple is hidden from the world,most of the people have been looking for it")
    print("You have completed the challenge! 👑")
def hidden_village():
    print("This is the village where you can find the information about the ancient medicines.")
    print("You have completed the challenge! 👑")
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

    
