MINIMUM_HEIGHT:int=50
def main():
    height=float(input("How old are you? "))
    if height>=MINIMUM_HEIGHT:
        print("You'r tall enough to ride!")
    else:
        print("You're not tall enough to ride,but may be next year! ")

if __name__ == '__main__':
    main()