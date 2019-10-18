import random

def populate_array_input():
    """ Gets user input for each element in the array.

    Returns:
        arr (list): The created array containing integers entered by the user.
    """
    arr = []
    while True:
        val = input("Enter a number, type a non-number to quit: ")
        try:
            val = int(val)
        except ValueError:
            break
        arr.append(val)
    return arr


def populate_array_random(arr_length):
    """ Creates an array of n random integers.

    Parameters:
        arr_length (int): The length of the array to be created.

    Returns:
        arr (list): The created array containing n random integers.
    """
    arr = []
    for i in range(int(arr_length)):
        arr.append(random.randint(-100000, 100000))
    return arr


def populate_array_decreasing(arr_length):
    """ Creates an array of n integers sorted in decreasing order.

    Parameters:
        arr_length (int): The length of the array to be created.

    Returns:
        arr (list): The created array containing n integers in decreasing order.
    """
    arr = []
    for i in range(int(arr_length)):
        arr.append(random.randint(-100000, 100000))
    arr.sort(reverse=True)
    return arr

def worstMergeSort(sorted_arr):
    """ Helper recursive method to arrange array elements into the worst case of mergesort.

    Parameters:
        sorted_arr (list): The array to be rearranged. The array must already be sorted in ascending order.

    Returns:
        worst_arr (list): The array as a combination of the left and right halves in the worst case.
    """
    # Base case
    if len(sorted_arr) <= 1:
        return sorted_arr

    # Partition left array with all the terms with even index
    left_arr = []
    for i in range(0, len(sorted_arr), 2):
        left_arr.append(sorted_arr[i])

    # Partition right array with all the terms with odd index
    right_arr = []
    for i in range(1, len(sorted_arr), 2):
        right_arr.append(sorted_arr[i])

    # Recursively divide the arrays into 2 until the base case for i in range(int(arr_length)):
    left_arr = worstMergeSort(left_arr)
    right_arr = worstMergeSort(right_arr)
    return left_arr + right_arr


def populate_array_worst(arr_length):
    """ Creates an array of n integers which provides the worst case of mergesort.

    Parameters:
        arr_length (int): The length of the array to be created.

    Returns:
        worst_arr (list): The created array containing n integers as the worst case of mergesort.
    """
    arr = []
    for i in range(int(arr_length)):
        arr.append(random.randint(-100000, 100000))
    arr.sort()    # sort into ascending order
    worst_arr = worstMergeSort(arr)
    return worst_arr