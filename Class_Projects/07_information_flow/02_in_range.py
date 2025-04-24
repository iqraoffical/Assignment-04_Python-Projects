def in_range(n, low, high):
  """
  Returns True if n is between low and high, inclusive. 
  high is guaranteed to be greater than low.

  """
  if n >= low and n <= high:
      return True
  return False
def main():
   n=int(input("Enter a number to check: "))
   low=int(input("Enter the lower bound: "))
   high=int(input("Enter the upper bound: "))

   if in_range(n,low,high):
      print(f"{n} is in the range {low} to {high}.")
   else:
      print(f"{n} is NOT in the range{low} to {high}.")
# Required to call the main function
if __name__ == '__main__':
    main()