# This is just a random list of numbers that are not sorted
unsorted_list = [10, 19, 12, 2, 5, 3, 13, 8, 6, 4]

# First we define the function that we will run
def BubbleSort(numbers):
    # This counter is just to tell us the amount of numbers in the list
    counter = len(numbers)
    print('Counter = ' + str(counter))
    # We set this to True so our loop runs
    swapped = True
    num = 0

    # The loop starts running
    while swapped:
        # We set this to false so that we force the loop to check all the numbers
        swapped = False
        # We go through all the numbers
        for num in range(counter - 1):
            # We check if the starting number is bigger than the next humber
            if unsorted_list[num] > unsorted_list[num + 1]:
                # If the starting number is bigger than the next number, we store its value
                swapnumber = unsorted_list[num]
                # Once we store the value of the starting number, we give it the value of the next number
                unsorted_list[num] = unsorted_list[num + 1]
                # Once the next number has its value taken, it now takes the value of the starting number that was saved
                unsorted_list[num + 1] = swapnumber
                # We force the check to run again until all the numbers are in the correct order

                swapped = True

    print(numbers)
if __name__ == '__main__':

    unsorted_list = [10, 19, 12, 2, 5, 3, 13, 8, 6, 4]

    BubbleSort(unsorted_list)
