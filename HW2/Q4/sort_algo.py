def ins_sort(arr):
    count = 0

    # iterate through the length of the list

    for i in range(0, len(arr)):
        count += 1
        key = arr[i]
        j = i - 1
        # Swap the elements in the list if the preceding element exceeds the succeeding element
        while j >= 1 and key < arr[j - 1]:
            count += 1
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
    print("The sorted array is: ", arr)

    return count


def main():

    arr = []
	# Define the array to operate on
    arr = 1024 * [1] + 2048 * [11] + 4096 * [111] + 1024 * [1111]

    print("Input data = ", arr)

    txt = open("output.txt", "w")

    for i in range(0, len(arr)):
        txt.write(str(arr[i]))
        txt.write("\n")

    print("The number of comparisons for the given data is: ", ins_sort(arr))


if __name__ == '__main__':
    main()
