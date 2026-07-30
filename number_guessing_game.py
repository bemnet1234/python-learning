import random
random_number = random.randint(1, 100)
guess = int(input("Guess a number between 1 and 100: "))
attempts = 1
while guess != random_number:
    if guess<random_number:
        print("Too low! Try again.")
    elif guess>random_number:
        print("Too high! Try again.")
    attempts=attempts + 1
    guess = int(input("Guess a number between 1 and 100: "))
print(f"Congratulations! You guessed the number {random_number} in {attempts} attempts.")