def get_user_numbers():
    """Create a list by entering a number"""
    user_numbers=[]
    while True:
      user_input=input("Enter a number: ")
      if user_input=="":
          break
      num=int(user_input)
      user_numbers.append(num)
    return user_numbers
def count_nums(num_lst):
    """Create an empty dictionary."""
    num_dict = {}
    for num in num_lst:
        if num not in num_dict:
            num_dict[num]=1
        else:
            num_dict[num]+=1
    return num_dict
def print_counts(num_dict):
    """
    Loop over the dictionary and print out each key and its value.
    """
    for num in num_dict:
        print(str(num) + " appears " + str(num_dict[num]) + " times.")


def main():
    """
    Ask the user to input numbers and store them in a list. Once they enter a blank line,
    print out the number of times each number appeared in the list.
    """
    user_numbers = get_user_numbers()
    num_dict = count_nums(user_numbers)
    print_counts(num_dict)


# Python boilerplate.
if __name__ == '__main__':
    main()

