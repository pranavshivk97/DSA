def shuffle(arr, left, right):

    # Calculate the mid point of the list/array
    mid = (left + (right - 1)) // 2

    i = arr[left]
    j = arr[mid]
    k = arr[right - 1]

    if i <= j <= k:
        return j, mid

    if k <= j <= i:
        return j, mid

    if i <= k <= j:
        return k, right - 1

    if j <= k <= i:
        return k, right - 1

    return i, left


def partition(arr, left, right):
    # Shuffle the array
    pe, pe_id = shuffle(arr, left, right)
    arr[left], arr[pe_id] = arr[pe_id], arr[left]

    i = left + 1
    for j in range(left + 1, right):
        if arr[j] < pe:
            # Swap the elements
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[left], arr[i - 1] = arr[i - 1], arr[left]

    return i - 1


def quicksort(arr, left, right):
    if left < right:
        pe_id = partition(arr, left, right)

        # Recursively sort each sub-array
        quicksort(arr, left, pe_id)
        quicksort(arr, pe_id + 1, right)

    return arr


def ins_sort_cutoff(arr, cutoff):
    # iterate through the length of the list

    for i in range(0, len(arr)):
        key = arr[i]
        j = i - 1
        # Swap the elements in the list if the preceding element exceeds the succeeding element
        while j >= 1 and key < arr[j - 1]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


def quicksort_cutoff(arr, left, N, right):
    
    N = 7
    if left < right:
        if right - left <= N:
            for i in range(left, right):
                k = arr[i]
                j = i - 1

                while j >= left and k < arr[j]:
                    arr[j + 1] = arr[j]
                    j -= 1

        l = partition(arr, left, right)
        quicksort_cutoff(arr, left, 7, l)
        quicksort_cutoff(arr, l + 1, 7, right)

    return arr


def quicksort_cutoff_inverion(arr, left, N, right):

    for N in range(10, 10000, 1000):
        if left < right:
            if right - left <= N:
                for i in range(left, right):
                    k = arr[i]
                    j = i - 1

                    while j >= left and k < arr[j]:
                        arr[j + 1] = arr[j]
                        j -= 1

            l = partition(arr, left, right)
            quicksort_cutoff(arr, left, N, l)
            quicksort_cutoff(arr, l + 1, N, right)

        return N, arr


def main():

    arr = []
    arr1 = []
    arr2 = []

    txt = input("Enter the file to open: ")

    txt1 = open(txt, 'r')

    for l in txt1:
        arr.append((int(l)))

    print("Input data is: ", arr, "\n")
    import time
    start1 = time.time()
    arr = quicksort(arr, 0, len(arr))
    stop1 = time.time()
    print("Time taken for the quicksort algorithm is: ", (stop1 - start1), "s.\n")
    # print("The sorted array using quicksort is:", arr)

    txt2 = open(txt, "r")
    for line in txt2:
        arr1.append(int(line))

    start2 = time.time()
    arr1 = quicksort_cutoff(arr1, 0, 7, len(arr1))
    stop2 = time.time()
    print("Time taken for the quicksort algorithm with insertion cutoff is: ", (stop2 - start2), "s.\n")
    # print("The sorted array using quicksort with the cutoff is: ", arr1)

    txt3 = open(txt, "r")
    for line in txt3:
        arr2.append(int(line))

    N = range(10, 10000, 100)
    start3 = time.time()
    arr2 = quicksort_cutoff_inverion(arr2, 0, N, len(arr2))
    stop3 = time.time()
    print("Performance: ", stop3 - start3, "s.\n")


if __name__ == '__main__':
    main()

