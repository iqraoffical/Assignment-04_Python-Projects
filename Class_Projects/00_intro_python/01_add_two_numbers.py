def main():
    print("This program adds two numbers.")

    #Promote the user to enter first number
    num1=int(input("Enter the first number:"))
    #Promote the user to enter second number
    num2=int(input("Enter the second number:"))
 
    #Sum of two numbers
    total_sum=num1+num2

    #Print the some of entered numbers
    print(f"The sum of {num1} and {num2} is {total_sum}")
# This provided line is required at the end of
    # Python file to call the main() function.
if __name__ == '__main__':
     main()

