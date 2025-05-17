import random

N_NUMBERS: int = 10
MIN_VALUE: int = 1
MAX_VALUE: int = 100

def main():
    """
    Prints 10 random integers between 1 and 100 (inclusive).
    """
    for _ in range(N_NUMBERS):
        value = random.randint(MIN_VALUE, MAX_VALUE)
        print(value)

if __name__ == '__main__':
    main()
