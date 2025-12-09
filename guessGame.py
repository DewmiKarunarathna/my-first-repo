{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "b49de236-b252-4415-8174-87634efee352",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "🎮Guess the number game!\n",
      "Select difficulity......\n",
      " 1 : Easy 😁\n",
      " 2 : Medium 😎\n",
      " 3 : Hard 😤\n",
      "------------------------------------\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter difficulity:  1\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "😏I am thinking about a number between 1 and 10\n",
      "\n",
      "You have 3 chances! 🤩\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "\n",
      "💭Attempt 1, your guess is :  6\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      " Too high👆 \n",
      " Only 2 attempts remain! 😬\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "\n",
      "💭Attempt 2, your guess is :  8\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      " Too high👆 \n",
      " Only 1 attempt remain! 😬\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "\n",
      "💭Attempt 3, your guess is :  9\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      " Too high👆 \n",
      " Oh you've lost! The number was 10 😢😢\n",
      "\n",
      " 💔Game over! The number was 10\n",
      "Thanks for playing!!😛\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "print(\"🎮Guess the number game!\")\n",
    "print(\"Select difficulity......\")\n",
    "print(\" 1 : Easy 😁\")\n",
    "print(\" 2 : Medium 😎\")\n",
    "print(\" 3 : Hard 😤\")\n",
    "print(\"------------------------------------\")\n",
    "max_num = 50\n",
    "max_attempts = 3\n",
    "\n",
    "choice = input(\"Enter difficulity: \")\n",
    "if choice == \"1\":\n",
    "    answer = random.randint(1,10)\n",
    "    max_attempts = 3    \n",
    "    max_num = 10\n",
    "elif choice == \"2\":\n",
    "    answer = random.randint(1,50)\n",
    "    max_attempts = 3 \n",
    "    max_num = 50\n",
    "elif choice == \"3\":\n",
    "    answer = random.randint(1,100)\n",
    "    max_attempts = 3 \n",
    "    max_num = 100\n",
    "else:\n",
    "    print(\"Invalid input 😬\")\n",
    "    print(\"Let's play medium difficulity! 😉\")\n",
    "print(f\"\\n😏I am thinking about a number between 1 and {max_num}\")\n",
    "print(f\"\\nYou have {max_attempts} chances! 🤩\")\n",
    "attempt = 0\n",
    "won = False\n",
    "while attempt < max_attempts and not won:\n",
    "    try:\n",
    "        guess = int(input(f\"\\n💭Attempt {attempt+1}, your guess is : \"))\n",
    "        if guess == answer:\n",
    "            print(f\"\\n🥳🥳🥳Hooray you've won! The number i was thinking is {answer}🥳🥳🥳\")\n",
    "            won = True\n",
    "\n",
    "        else:\n",
    "            attempt +=1\n",
    "            remaining = max_attempts - attempt\n",
    "            if answer<guess:\n",
    "                print(f\"\\n Too low 👇\" , end=\" \")\n",
    "            else:\n",
    "                print(f\"\\n Too high👆\" , end=\" \")\n",
    "                if remaining > 0:\n",
    "                    print(f\"\\n Only {remaining} attempt{'s' if remaining > 1 else ''} remain! 😬\")  \n",
    "                else:\n",
    "                    \n",
    "                    print(f\"\\n Oh you've lost! The number was {answer} 😢😢\")\n",
    "    except ValueError:\n",
    "        print(\"❌ Please enter a valid number!\")\n",
    "if not won and attempt == max_attempts :\n",
    "    print(f\"\\n 💔Game over! The number was {answer}\")  \n",
    "    print(\"Thanks for playing!!😛\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f4903295-5cd4-46de-97f8-6f315432c9fb",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
