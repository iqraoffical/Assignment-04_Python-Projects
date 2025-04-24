def main():
    number:float=float(input("Type a number to see its square:"))
    # square is equal to two times of number
    square=number * number

    # Logic to square the number
    print(str(number)+ "squared is" + str(number ** 2))
    
    # print the result of squared number
    print(f"{number} squared is {square}")

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()