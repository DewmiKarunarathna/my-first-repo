import random
#function to re-play the game
def replay():
    choice = input("⭐Do you want to play again(y/n): ").strip().lower()  #strip to remove spaces and lower to transform everything into lowercase
    if choice in ['y',"yes","yeah"]:
        return True
    elif choice in ['n',"no","nope"]:
        return False
    else:
        print("Invalid input")
        replay()
#greeting the player function
def greet():
    name = input("Please enter your name: ").strip()
    return name if name else "Player"
#hint system - odd number or even number
def hint(answer):
    if answer%2==0:
        print("The number is an even number 😏!")
    else:
        print("The number is an odd number 😏!")
score = 0        
while True:
    print("🎮Guess the number game!")
    name = greet()
    print(f"\n Hello {name}! Welcome to the number guessing game")
    print("Select difficulity......")
    print(" 1 : Easy 😁")
    print(" 2 : Medium 😎")
    print(" 3 : Hard 😤")
    print("------------------------------------")
    max_num = 50
    max_attempts = 3
    choice = input("Enter difficulity: ")
    if choice == "1":
        answer = random.randint(1,10)
        max_attempts = 3    
        max_num = 10
    elif choice == "2":
        answer = random.randint(1,50)
        max_attempts = 3 
        max_num = 50
    elif choice == "3":
        answer = random.randint(1,100)
        max_attempts = 3 
        max_num = 100
    else:
        print("Invalid input 😬")
        print("Let's play medium difficulity! 😉")
    print(f"\n😏I am thinking about a number between 1 and {max_num}")
    print(f"\nYou have {max_attempts} chances! 🤩")
    attempt = 0
    won = False
    while attempt < max_attempts and not won:
        try:
            if attempt==2:
                    ask_hint = input("Doy you want a hint? (y/n)")
                    if ask_hint=="y":
                        hint(answer)
            guess = int(input(f"\n💭Attempt {attempt+1}, your guess is : "))
            if guess == answer:
                
                print(f"\n🥳🥳🥳Hooray you've won! The number i was thinking is {answer}🥳🥳🥳")
                won = True
            else:
                attempt +=1
                remaining = max_attempts - attempt
                if guess<answer:
                    print(f"\n Too low 👇" , end=" ")
                else:
                    print(f"\n Too high👆" , end=" ")
                    if remaining > 0:
                        print(f"\n Only {remaining} attempt{'s' if remaining > 1 else ''} remain! 😬")  
                    else:
                        print(f"\n Oh you've lost! The number was {answer} 😢😢")
        except ValueError:
            print("❌ Please enter a valid number!")
    if not won and attempt == max_attempts :
        print(f"\n 💔Game over! The number was {answer}")  
        print(f"Thanks for playing {name}!!😛")
    if won:
        score = (1000-(attempt+1)*2)*max_num
        print(f"Your score is {score}! Well done ☺️")
    if not replay():
        break
