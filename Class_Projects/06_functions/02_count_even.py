def count_even(lst=None):
    if lst is None:
        lst=[]
        while True:
          user_input=input("Enter an integer or press enter to stop:")
          if user_input=="":
             break
          try:
              number=int(user_input)
              lst.append(number)
          except ValueError:
              print("Please enter a valid integer.")

    even_count = 0
    for num in lst:
        if num % 2 == 0:
            even_count += 1

    print("Number of even numbers:", even_count)

