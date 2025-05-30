import random
NUM_ROUNDS=5

def main():
    print("Welcome to the High_Low Game!")
    print('----------------------------------')
    your_score=0

    # Milestone 4: Play multiple rounds
    for i in range(NUM_ROUNDS):
        print("Round",i+1)
        computer_num:int=random.randint(1,100)
        your_num:int=random.randint(1,100)
        print("Your  number is",your_num)

        # Milestone 2: Get user input for their choice
        choice:str=input("Do you think your number is higher or lower than the computer's")
        while choice!="higher" and choice!="lower":
            choice=input("Please enter either higher or lower:")

        # Milestone 3: Map out all the ways to win the round
        higher_and_correct:bool=choice=="higher" and your_num>computer_num
        lower_and_correct:bool=choice=="lower" and your_num <computer_num

        if higher_and_correct or lower_and_correct:
            print("You were right! The computer's number was", computer_num)
        # Milestone 5: keep track of your score
        your_score+=1
    else:
        print("Aww, that's incorrect. The computer's number was", computer_num)

        # Milestone 5: keep track of your score
        print("Your score is now", your_score)
        print()
        if your_score==NUM_ROUNDS:
            print("Wow! You played perfectly!")
        elif your_score>NUM_ROUNDS//2:
           print("Good job, you played really well!")
        else:
            print("Better luck next time!")

if __name__ == "__main__":
    main()