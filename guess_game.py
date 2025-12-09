import random
print("🎮Guess the number game!")
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
        guess = int(input(f"\n💭Attempt {attempt+1}, your guess is : "))
        if guess == answer:
            print(f"\n🥳🥳🥳Hooray you've won! The number i was thinking is {answer}🥳🥳🥳")
            won = True

        else:
            attempt +=1
            remaining = max_attempts - attempt
            if answer<guess:
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
    print("Thanks for playing!!😛")
