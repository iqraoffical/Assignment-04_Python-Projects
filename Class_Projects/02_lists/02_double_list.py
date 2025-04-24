def main():
    numbers:list[int]=[1,2,3,4]
    for i in range(len(numbers)):#Loop through the indices of the list
        elem_at_index=numbers[i]#Get the elemnt in the index list
        numbers[i]=elem_at_index*2 #Set the element to 2 time of the previous element
    print(numbers) #printout the numbers

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()