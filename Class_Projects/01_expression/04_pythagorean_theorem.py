import math # Import the math library so we can use the sqrt function
def main():
    #Get the length of two sides from user
    ab:float=float(input("Enter the length of ab:"))
    ac:float=float(input("Enter the length of ac:"))

    # Calculate the hypotenuse using the two sides and print it out
    bc:float=math.sqrt(ab**2+ac**2)
    print(f"The length of BC(the hypotenuse) is: {bc}")
# There is no need to edit code beyond this point

if __name__ == '__main__':
 main()