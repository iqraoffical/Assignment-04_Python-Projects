def add_many_numbers(numbers: list[int]) -> int:
    """Takes a list of numbers and returns the sum of those numbers"""
    total: int = 0 
    for number in numbers:
        total += number
    return total

# There is no need to edit code beyond this point
def main():
    numbers: list[int] = [1, 2, 3, 4, 5] 
    sum_of_numbers: int = add_many_numbers(numbers)
    print(sum_of_numbers)

if __name__ == '__main__':
    main()
