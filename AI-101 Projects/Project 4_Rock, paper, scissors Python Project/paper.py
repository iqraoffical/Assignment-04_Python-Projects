import random
def rock_paper_scissors():
 print("Welcome to the Rock,Paper,Scissors!")
options=["rock","paper","scissors"]
while True:
        user_choice=input("Enter rock,paper,or sscissors (or 'exit to quit): ").lower()
        if user_choice=='exit':
            print ("Thanks for playing!")
            break
        if user_choice not in options:
            print("Invalid choice.Try again.\n")
            continue 
        computer_choice=random.choice(options)
        print(f"You choose:{user_choice}")
        print(f"Computer choose:{computer_choice}")

        if user_choice==computer_choice:
            print("It's a tie!\n")
        elif (user_choice=="rock" and computer_choice=="scissors") or\
            (user_choice=="paper" and computer_choice=="rock") or\
            (user_choice =="paper" and computer_choice=="rock"):
            print("You win!\n")
        else:
            print("You lose!\n")

if __name__ == "__main__":
    rock_paper_scissors()
