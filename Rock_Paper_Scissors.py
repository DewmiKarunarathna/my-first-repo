#simple rock paper scissor game
import random
def instruction():
    print("👾How to play")
    print("1. Enter your name!")
    print("2. Select difficluity : Easy | Medium | Hard ")
    print("3. Enter the right choice")
    print("4. Win within limited attempts!")
    print("Good luck🤞🍀!")
def ins2():
    print("Press 1 for rock 🪨")
    print("Press 2 for Paper 📃")
    print("Press 3 for Scissor ✂️")
def greet():
    name = input("Please enter your name: ").strip()
    return name if name else "Player"    
def game(choice,choices):
    computer_score = 0
    user_score = 0
    computer_choice = random.choice(choices) 
    try:
        choice = int(choice)
    except:
        return computer_score, user_score  # Return 0,0 for invalid input
    if choice == 1 and computer_choice== "Paper 📃":
        computer_score+=1
        print("Yikes! Paper covers the rock 😏")
    elif choice == 1 and computer_choice == "Scissor ✂️":
        user_score+=1
        print("Rock crushed the scissor! 😯")
    elif choice == 2 and computer_choice == "Rock 🪨":
        user_score+=1
        print("Nice! Paper covers the rock 🙂‍↔️")
    elif choice == 2 and computer_choice == "Scissor ✂️":
        computer_score +=1
        print("Oops! Scissor cuts the paper 😥")
    elif choice == 3 and computer_choice == "Rock 🪨":
        computer_score+=1
        print("NOOO! Rock crushed the scissor! 😯")
    elif choice == 3 and computer_choice == "Paper 📃":
        user_score+=1
        print("Scissor cuts the paper 😉")
    elif choice in [1, 2, 3] and ["Rock 🪨", "Paper 📃", "Scissor ✂️"][choice-1] == computer_choice:
        print("It's a tie! 🤝")    
    else:
        print("Oh no invalid input!")
    return computer_score, user_score    
def save_score(name, score):
    with open("Scores.txt","a") as f: #a means append the marks, and it creates a new text file if there is no such file like that
        f.write(f"{name}: {score}\n")    
def show_logo():
    print(r"""
    ┌─────────────────────────────────────┐
              │  ROCK  ✋ PAPER  ✌️ SCISSORS       │
              └─────────────────────────────────────┘""")    
    print("Hello! Welcome to the Rock Paper Scissors game")
choices = ["Rock 🪨", "Paper 📃","Scissor ✂️"]
def replay(): #replay function
    choice = input("⭐Do you want to play again(y/n): ").strip().lower() 
    if choice in ['y',"yes","yeah"]:
        return True
    elif choice in ['n',"no","nope"]:
        return False
    else:
        print("Invalid input")
        return replay()

while True:
    show_logo()
    name = greet()
    print(f"Hello {name} Welcome to Rock, Paper, Scissors game")
    replay_choice = int(input("Do you want instructions? Press 1 for instructions and any other key for continue!"))
    if replay_choice == 1:
        instruction()
    print (choices)
    print("Select difficulity level 😤")
    print("1 - Easy 😊")
    print("2 - Medium 😁")
    print("2 - Hard 🤯")
    level = int(input("Enter level: "))
    chances = 0  
    score_user = 0
    score_computer = 0
    if level == 1:
        chances = 5
    elif level == 2:
        chances = 10
    elif level == 3:
        chances = 15
    else:
        print("Hmm..invalid input! Let's play level 2 😏")
    print(f"\nYou have {chances} rounds to play!")    
    while chances>0:
        ins2()
        choice = input("Enter your choice: ")
        chances-=1
        score = game(choice, choices)
        score_user+=score[1]
        score_computer = score[0]
    if score_user >= score_computer :
        print(f"You won ! Wow 🥳🥳🥳 Your score is {score_user}!")
    else:
        print(f"Awww you've lost! Better luck next time! 💔💔Your score is {score_user}!")
    save_score(name, score_user)    
    if not replay():
        break
        
                
