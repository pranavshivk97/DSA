# Function for merging the sub-arrays
def merge(arr, left, mid, right):
    count = 0

    # Defining limits for each sub-array
    n1 = mid - left + 1
    n2 = right - mid

    left_arr = []
    right_arr = []

    # Adding elements to the sub-arrays
    for i in range(0, n1):
        left_arr.append(arr[left + i])

    for j in range(0, n2):
        right_arr.append(arr[mid + 1 + j])

    i = j = 0
    k = left
    # Sort the elements in each subarray by using auxiliary array arr
    # First, add elements of the left/right sub-array, whichever is bigger
    while i < n1 and j < n2:
        if left_arr[i] < right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
            count += 1

        else:
            arr[k] = right_arr[j]
            j += 1
            count += 1

        k += 1

    # Then, add the second sub-array's elements
    while i < n1:
        arr[k] = left_arr[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = right_arr[j]
        j += 1
        k += 1

    # print("The sorted array is: ", arr, "\n")
    return count


def recursive_merge(arr, left, right):
    count = 0

    import time
    start = time.time()

    if right > left:
        mid = (left + right) // 2

        # Sort the left sub array, by recursively sorting the left half then the right half
        count += recursive_merge(arr, left, mid)
        count += recursive_merge(arr, mid + 1, right)
        count += merge(arr, left, mid, right)
    stop = time.time()

    return count


def botup_merge(arr):
    count = 0
    sz = 1

    import time
    start = time.time()
    while sz < len(arr) - 1:
        left = 0
        while left < len(arr) - 1:
            mid = left + sz - 1

            if left + 2*sz - 1 > len(arr) - 1:
                right = len(arr) - 1
            else:
                right = left + 2*sz - 1

            count += merge(arr, left, mid, right)
            left += 2*sz
        sz *= 2

    stop = time.time()
    print("Relative wall clock time (BOTTOM UP): ", (stop - start), "s.\n")
    # print("The sorted array using bottom up merge sort is: ", arr, "\n")
    return count


def main():
    arr = []
    arr2=[]
    txt = input("Enter the file to open: ")

    txt1 = open(txt, 'r')

    for l in txt1:
        arr.append(int(l))

    for p in arr:
        arr2.append(int(p))

    # print(arr2)
    import time
    start = time.time()
    print("The number of comparisons in RECURSIVE MERGE SORT is: ", recursive_merge(arr, 0, len(arr) - 1))
    print("The physical wall clock time taken for RECURSIVE MERGE SORT: ", (time.time() - start))
    print("The number of comparisons in BOTTOM UP MERGE SORT is: ", botup_merge(arr2))


if __name__ == '__main__':
    main()
