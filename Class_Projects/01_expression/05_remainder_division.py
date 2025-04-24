def main():
    # Get input from the user
    dividend: int = int(input("Please enter an integer to be divided: "))
    divisor: int = int(input("Please enter an integer to divide by: "))

    # Perform integer division
    quotient: int = dividend // divisor  # Integer division (no decimals)
    remainder: int = dividend % divisor  # Remainder after division

    # Display the results
    print(f"Quotient: {quotient}")
    print(f"Remainder: {remainder}")  # Fixed the typo here

# This ensures the main function runs when the script is executed directly
if __name__ == '__main__':
    main()
