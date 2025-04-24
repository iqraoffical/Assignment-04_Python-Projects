def read_phone_numbers():
    """
    Ask the user for names and numbers to store in a phonebook (dictionary).
    Returns the phonebook.
    """
    phonebook = {}

    print("Enter contact names and numbers. Leave name empty to finish.")
    while True:
        name = input("Name: ").strip()
        if not name:
            break
        number = input("Number: ").strip()
        phonebook[name] = number

    return phonebook


def print_phonebook(phonebook):
    """
    Prints out all the names and numbers in the phonebook.
    """
    print("\nPhonebook Entries:")
    if not phonebook:
        print("Phonebook is empty.")
    else:
        for name, number in phonebook.items():
            print(f"{name} -> {number}")


def lookup_numbers(phonebook):
    """
    Allow the user to look up phone numbers by name.
    """
    print("\nPhonebook Lookup. Leave blank to exit.")
    while True:
        name = input("Enter name to look up: ").strip()
        if not name:
            break
        if name in phonebook:
            print(f"{name}'s number: {phonebook[name]}")
        else:
            print(f"{name} is not in the phonebook.")


def main():
    phonebook = read_phone_numbers()
    print_phonebook(phonebook)
    lookup_numbers(phonebook)


if __name__ == "__main__":
    main()
