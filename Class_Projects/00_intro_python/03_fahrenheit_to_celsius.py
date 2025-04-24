

def main():
    # Prompt the user to enter a temperature in Fahrenheit
    degrees_fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    
    # Convert Fahrenheit to Celsius 
    degrees_celsius = (degrees_fahrenheit - 32) * 5.0 / 9.0
    
    # Display the converted temperature
    print(f"Temperature: {degrees_fahrenheit}F = {degrees_celsius}C")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == "__main__":
    main()
