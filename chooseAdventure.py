#choose your own adventure game
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
