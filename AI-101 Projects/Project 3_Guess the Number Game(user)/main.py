def computer_guesses_number():
    print("Think of a number between 1 and 100 and I will try to guess it!")
    input("Press Enter when you're ready...")

    low = 1
    high = 100
    attempts = 0
    while low <= high:
        guess = (low + high) // 2
        attempts += 1
        print(f"My guess is: {guess}")
        feedback = input("Is it too high (H), too low (L), or correct (C)? ").strip().upper()
        if feedback == 'H':
            high = guess - 1
        elif feedback == 'L':
            low = guess + 1
        elif feedback == 'C':
            print(f"Yay! I guessed your number {guess} in {attempts} tries.")
            break
        else:
            print("Invalid input. Please enter 'H', 'L', or 'C'.")

if __name__ == "__main__":
    computer_guesses_number()