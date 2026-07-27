while True:
    inp=input("Roll the dice? (y/n): ")
    if inp.lower() == "y":
        import random
        dice_roll = random.randint(1, 6)
        dice_roll1 = random.randint(1, 6)
        print(f"({dice_roll}, {dice_roll1})")
    elif inp.lower() == "n":
        print("Thanks for playing!")
        break   
    else: 
        print("Invalid input. Please enter 'y' or 'n'.")