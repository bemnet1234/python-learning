import random
while True:
    user_choice=input("rock, paper, scissors(r, p, s): ").lower()
    computer_choice=random.choice(["r", "p", "s"])
    choices= {
        "r": "🪨",
        "p": "📄",
        "s": "✂️"
    }
    print(f"You chose {choices[user_choice]}")
    print(f"Computer chose {choices[computer_choice]}")
    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == "r" and computer_choice == "s":
        print("You win!")
    elif user_choice == "p" and computer_choice == "r":
        print("You win!")
    elif user_choice == "s" and computer_choice == "p":
        print("You win!")
    else:
        print("Computer wins!")
    continue_choice = input("continue? (y/n): ")
    if continue_choice != "y":
        break
