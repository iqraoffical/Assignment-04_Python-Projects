import random

def hangman():
    words=["python","hangman","challenge","project"]
    word=random.choice(words)
    guessed="_"* len(word)
    attempts=6
    guessed_letters=[]

    print("Welcome to the Hangman!")
    while attempts>0 and "_" in guessed:
     print(f"\nWord:{guessed}")
     print(f"Guessed Letters:{guessed_letters}")
     print(f"Attempts left:{attempts}")
     guess=input("Guess a letters").lower()

     if guess in guessed_letters:
        print("You already guessed that.")
     elif guess in word:
        guessed_letters.append(guess)
        guessed = "".join([letter if letter in guessed_letters else "_" for letter in word])
     else:
        guessed_letters.append(guess)
        attempts-=1
        print("Wrong guess!")
    print("\nYou won!" if "_" not in guessed else f"You lost! The word was '{word}'.")

   
if __name__== "__main__":
      hangman()