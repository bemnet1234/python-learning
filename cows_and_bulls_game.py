def generate_a_4_digit_number():
    import random
    return str(random.randint(1000,9999))
def get_user_guess():
    guess = input("Guess: ")
    while len(guess) !=4 or not guess.isdigit():
        guess = input("Invalid input. Please enter a 4 digit number: ")
    return guess
def check_cows_and_bulls(secret_number, user_guess):
    cows = sum(1 for s, g in zip(secret_number, user_guess) if s == g)
    bulls = sum(1 for digit in user_guess if digit in secret_number) - cows
    return cows, bulls
def main():
    secret_number = generate_a_4_digit_number()
    print("I have generated a 4 digit number. Try to guess it!\n")
    attempts = 0
    while True:
        user_guess = get_user_guess()
        attempts += 1
        cows, bulls = check_cows_and_bulls(secret_number, user_guess)
        print(f"{cows} Cows, {bulls} Bulls")
        if cows == 4:
            print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
            break

if __name__ == "__main__":
    main()

