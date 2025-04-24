def main():
    #get the 3 sides of lengths of the triangle
    side1: float=float(input("What is the length of side 1?"))
    side2: float=float(input("What is the length of side 2?"))
    side3:float=float(input("What is the length of side 3?"))
    perimeter=side1+side2+side3
   
    #Print out the perimeter of triangle
    print(f"The perimeter of the triangle is {perimeter}")

# There is no need to edit code beyond this point
if __name__== "__main__":
        main()