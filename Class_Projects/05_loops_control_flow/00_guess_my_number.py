
import random 
def main():
    # generate random secret number
    secret_number=random.randint(1,99)
    print("I am thinking of a number between 1 and 99...")

    # get user guess
    guess=int(input("Enter a guess:"))

    # condition

    # If-statement is True if guess is less than secret number

    while guess!=secret_number:
        if guess< secret_number:
            print("Your guess is too low")
        else:
            print("Your guess is too high")
        print()
        guess=int(input("Enter a new guess: "))

        print("Congrats! The number was : "+ str(secret_number))
if __name__ == '__main__':
    main()