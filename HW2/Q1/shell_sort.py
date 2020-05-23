# function for demonstrating the insertion sort algorithm
def ins_sort(arr):
    count = 0

    # iterate through the length of the list
    for i in range(1, len(arr)):
        count += 1
        key = arr[i]
        j = i - 1
        # Swap the elements in the list if the preceding element exceeds the succeeding element
        while j >= 0 and key < arr[j]:
            count += 1
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return count, arr

# Shell sort function that takes parameters as the array and the gap to consider (n)
def shell_sort(arr, n):
    count = 0
	# iterate throughout the length of the array beginning from the gap 
    for i in range(n, len(arr)):
        count += 1
        key = arr[i]
        j = i
		
		# h-sort the arrays
        while j >= n and arr[j - n] > key:
            count += 1
            arr[j] = arr[j - n]

            j -= n

        arr[j] = key

    return count, arr


def main():
    arr = []
    arr1 = []

    # Reading the file and copying to a list
    txt = input("Enter the file to open: ")
    txt1 = open(txt, "r")

    for k in txt1:
        arr.append(int(k))

    print("Input Data: ", arr)
    print("\n")

    count = count1 = count2 = count4 = count5 = 0
	
	# calculate elapsed time
    import time
    start1 = time.time()
    count, arr = shell_sort(arr, 7)
    count1, arr = shell_sort(arr, 3)
    count2, arr = ins_sort(arr)
    stop1 = time.time()
    # print("The sorted array is: ", arr)

    txt2 = open(txt, "r")

    for line in txt2:
        arr1.append(int(line))

    start2 = time.time()
    count3, arr1 = shell_sort(arr1, 7)
    count4, arr1 = shell_sort(arr1, 3)
    count5, arr1 = shell_sort(arr1, 1)
    stop2 = time.time()
    # print("The sorted array is: ", arr1)

    # print the results obtained
    print("Number of comparisons for shell sort phase is: ", count + count1)
    print("Number of comparisons for insertion sort phase is: ", count2, "\n")
    print("COMPARISONS:")
    print("Shell sort reverting to insertion sort: ", count + count1 + count2)
    print("Shell sort all the way: ", count3 + count4 + count5)

    print("PHYSICAL WALL CLOCK TIME:")
    print("Shell sort reverting to insertion sort: ", (stop1 - start1), "s.")
    print("Shell sort all the way: ", stop2 - start1, "s.")


if __name__ == '__main__':
    main()
